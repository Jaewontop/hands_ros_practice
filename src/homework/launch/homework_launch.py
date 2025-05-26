from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='homework',
            executable='publisher_node',
            name='publisher_node'
        ),
        Node(
            package='homework',
            executable='subscriber_node',
            name='subscriber_node'
        ),
    ]) 