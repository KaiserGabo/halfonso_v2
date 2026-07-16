import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch_ros.actions import Node


def generate_launch_description():

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',  # Defaults to True as requested
        description='Nav2 configuration for real time application'
    )

    use_sim_time = LaunchConfiguration('use_sim_time')

    include_navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time
        }.items()
    )

    explorer_node = Node(
        package='custom_explorer',
        executable='explorer',
        name='explorer_node',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time
        }]
    )

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time)
    ld.add_action(include_navigation)
    ld.add_action(explorer_node)

    return ld
