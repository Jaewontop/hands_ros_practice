import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, Bool
import random
from rclpy.qos import QoSProfile

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(Float64MultiArray, '/random_array', qos_profile)
        self.subscription = self.create_subscription(Bool, '/bool_result', self.bool_callback, qos_profile)
        self.subscription  # prevent unused variable warning
        self.bool_data = None
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data = [random.random(), random.random()]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published random array: {msg.data}')

    def bool_callback(self, msg):
        self.bool_data = msg.data
        self.get_logger().info(f'Received Bool: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 