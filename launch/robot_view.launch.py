import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    package_name = "halfonso_v2"
    package_dir = get_package_share_directory(package_name)

    # Optional saved RViz config path
    default_rviz_config_path = os.path.join(package_dir, "config", "view_robot.rviz")

    rviz_config_arg = DeclareLaunchArgument(
        "rviz_config",
        default_value=default_rviz_config_path,
        description="Full path to the RViz configuration file to use",
    )

    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="Use simulation time if true",
    )

    # RViz2 Node
    # Passes no local robot description — it subscribes directly over DDS
    node_rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", LaunchConfiguration("rviz_config")],
        parameters=[{"use_sim_time": LaunchConfiguration("use_sim_time")}],
    )

    ld = LaunchDescription()
    ld.add_action(rviz_config_arg)
    ld.add_action(use_sim_time_arg)
    ld.add_action(node_rviz)

    return ld
