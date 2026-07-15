from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import LifecycleNode, Node
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
import lifecycle_msgs.msg
import os


def generate_launch_description():
    # Get the package's share directory
    share_dir = get_package_share_directory('halfonso_v2')
    rviz_config_file = os.path.join(share_dir, 'config', 'halfonso_config.rviz')


    rviz2_node = Node(package='rviz2',
                      executable='rviz2',
                      name='rviz2',
                      arguments=['-d', rviz_config_file],
                      parameters=[{
                          'scan_qos_profile': 'BEST_EFFORT'  # Set QoS for RViz2 to Reliable
                      }],
                      )
    # Return the launch description
    return LaunchDescription([
        rviz2_node
    ])
