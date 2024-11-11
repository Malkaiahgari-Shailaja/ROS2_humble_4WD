from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    package_dir = os.path.join(get_package_share_directory('four_wheel_robot'))
    urdf_file = os.path.join(package_dir, 'urdf', 'four_wheel_robot.urdf.xacro')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': Command(['xacro ', urdf_file])}]
        ),
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_controller'],
            output='screen'
        ),
    ])
