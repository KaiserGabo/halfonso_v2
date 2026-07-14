import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg = get_package_share_directory('halfonso_v2')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg, 'launch', 'rsp.launch.py')),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            os.path.join(pkg, 'config', 'diff_drive.yaml'),
            {'use_sim_time': use_sim_time}
        ],
        output='screen',
    )

    spawn_controllers = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller', 'joint_state_broadcaster'],
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        robot_state_publisher,
        controller_manager,
        spawn_controllers,
    ])
