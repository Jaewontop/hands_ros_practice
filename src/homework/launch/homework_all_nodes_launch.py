from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='homework',
            executable='node1',
            name='node1'
        ),
        Node(
            package='homework',
            executable='node2',
            name='node2'
        ),
        Node(
            package='homework',
            executable='node3',
            name='node3'
        ),
    ]) 