import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    package_name = "halfonso_v2"
    package_dir = get_package_share_directory(package_name)

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

    gmapping_launch = Node(
        package='slam_gmapping',
        executable='slam_gmapping',
        output='screen',
        parameters=[os.path.join(get_package_share_directory(
            package_dir), "config", "slam_gmapping.yaml")]
    ),

    b_link_2_b_laser_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_to_base_laser',
        arguments=['-0.0046412', '0', '0.094079', '0', '0', '0', 'base_link', 'laser_frame']
    ),

    b_foot_2_b_link = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_foot',
        arguments=['-0.0', '0', '0.0', '0', '0', '0', 'base_footprint', 'base_link']
    ),

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
    ld.add_action(gmapping_launch)
    ld.add_action(b_link_2_b_laser_tf)
    ld.add_action(b_foot_2_b_link)
    ld.add_action(explorer_node)

    return ld
