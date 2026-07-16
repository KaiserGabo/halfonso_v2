import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    RegisterEventHandler,
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.event_handlers import OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import LifecycleNode

# Image Transport Republishers
# terminal command example: ros2 run image_transport republish raw compressed --ros-args -r in:=/camera/image_raw -r out/compressed:=/camera/image_raw/compressed
def image_transport_republisher(transport, camera_topics):
    base_topic = camera_topics.split("/")[-1]

    return Node(
        package="image_transport",
        executable="republish",
        name=f"image_transport_republish_{transport}_{base_topic}",
        arguments=["raw", transport],
        remappings=[
            ("in", f"/camera/{camera_topics}"),
            (f"out/{transport}", f"/camera/{camera_topics}/{transport}"),
        ],
    )


def generate_launch_description():

    package_name = "halfonso_v2"
    package_dir = get_package_share_directory(package_name)
    lidar_params = LaunchConfiguration('params_file')

    use_sim_time = LaunchConfiguration("use_sim_time")
    use_ros2_control = LaunchConfiguration("use_ros2_control")
    # lidar_serial_port = LaunchConfiguration("lidar_serial_port")

    declare_use_sim_time = DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="If true, use simulated clock",
    )

    declare_use_ros2_control = DeclareLaunchArgument(
        "use_ros2_control",
        default_value="true",
        description="If true, use ros2_control",
    )

    params_declare = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(package_dir, 'config', 'ydlidar.yaml'),
        # You can change the .yaml file depending on your lidar,
        # ydlidar.yaml is a copy of TminiPro.yaml in this project,
        # see ydlidar_base.yaml for a basic format of the lidar parameters
        description='Path to the ROS2 parameters file to use.'
    )

    # declare_lidar_serial_port = DeclareLaunchArgument(
    #     'lidar_serial_port',
    #     default_value='/dev/ttyUSB1',
    #     description='Specifying usb port to connected lidar'
    # )

    # Declare the path to files
    robot_description_xacro_file = os.path.join(
        package_dir, "description", "robot.urdf.xacro"
    )

    rviz_config_file_dir = os.path.join(package_dir, "config", "halfonso_config.rviz")

    robot_controllers_file_dir = os.path.join(package_dir, "config", "controller.yaml")

    twist_mux_params_file = os.path.join(package_dir, "config", "twist_mux.yaml")

    # robot_state_publisher setup
    robot_description_config = Command(
        [
            "xacro ",
            robot_description_xacro_file,
            " use_ros2_control:=",
            use_ros2_control,
        ]
    )

    params = {
        "robot_description": ParameterValue(robot_description_config, value_type=str),
        "use_sim_time": use_sim_time,
        "use_ros2_control": use_ros2_control,
    }

    # robot_state_publisher node
    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    # Image Transport Republishers Node
    # camera = 'image_raw'
    # depth_camera = 'depth/image_raw'
    # image_transports = ['compressed','compressedDepth', 'theora', 'zstd' ]
    # node_image_republishers = [image_transport_republisher(transport, depth_camera)
    #                       for transport in image_transports]

    # controller spawn
    node_ros2_control = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[params, robot_controllers_file_dir],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    diff_drive_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller", "--param-file", robot_controllers_file_dir],
    )

    node_twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        name="twist_mux",
        output="screen",
        parameters=[
            twist_mux_params_file,
            {"use_stamped": True},
        ],
        remappings=[
            ("cmd_vel_out", "diff_drive_controller/cmd_vel"),
        ],
    )

    node_twist_stamper = Node(
        package="twist_stamper",
        executable="twist_stamper",
        name="twist_stamper",
        output="screen",
        remappings=[
            ("cmd_vel_in", "cmd_vel_smoothed"),
            ("cmd_vel_out", "nav_vel"),
        ],
    )

    register_node_ros2_control = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=node_robot_state_publisher,
            on_start=[node_ros2_control],
        )
    )

    register_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=node_ros2_control,
            on_start=[joint_state_broadcaster_spawner],
        )
    )

    register_diff_drive_controller_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=joint_state_broadcaster_spawner,
            on_start=[diff_drive_controller_spawner],
        )
    )

    # node_ydlidar_drive = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         [
    #             os.path.join(
    #                 get_package_share_directory("ydlidar_ros2_driver"),
    #                 "launch",
    #                 "ydlidar_launch.py",
    #             )
    #         ]
    #     ),
    #     launch_arguments={
    #         'serial_port': lidar_serial_port,
    #         'frame_id': 'lidar_frame'
    #         }.items()

    # )

    node_ydlidar_drive = LifecycleNode(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_ros2_driver_node',
        namespace='/',
        output='screen',
        emulate_tty=True,
        parameters=[lidar_params],
    )

    tf2_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_pub_laser',
        arguments=['0', '0', '0.02', '0', '0', '0', '1', 'base_link', 'laser_frame'],
    )

    

    # Create the launch description and populate
    ld = LaunchDescription()

    # Add the nodes to the launch description
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_use_ros2_control)
    # ld.add_action(declare_lidar_serial_port)

    ld.add_action(register_node_ros2_control)
    ld.add_action(register_joint_state_broadcaster_spawner)
    ld.add_action(register_diff_drive_controller_spawner)
    ld.add_action(params)
    ld.add_action(node_ydlidar_drive)
    ld.add_action(tf2_node)

    ld.add_action(node_robot_state_publisher)
    ld.add_action(node_twist_mux)
    ld.add_action(node_twist_stamper)
    # for node_republisher in node_image_republishers:
    #     ld.add_action(node_republisher)
    # ld.add_action(node_ydlidar_drive)

    # Generate the launch description
    return ld
