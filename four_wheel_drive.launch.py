# ~/4wd_robot_ws/src/four_wheel_drive/launch/four_wheel_drive.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='four_wheel_drive',
            executable='control_node',
            output='screen'
        ),
    ])
