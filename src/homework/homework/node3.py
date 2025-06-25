import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from rclpy.qos import QoSProfile

class Node3(Node):
    def __init__(self):
        super().__init__('node3')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(Twist, '/twist_topic', self.twist_callback, qos_profile)
        self.publisher_ = self.create_publisher(Bool, '/bool_result', qos_profile)
        self.subscription  # prevent unused variable warning

    def twist_callback(self, msg):
        bool_msg = Bool()
        bool_msg.data = False if msg.linear.x == 0.0 else True
        self.publisher_.publish(bool_msg)
        self.get_logger().info(f'Published Bool: {bool_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 