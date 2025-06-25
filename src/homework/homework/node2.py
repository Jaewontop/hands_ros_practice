import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class Node2(Node):
    def __init__(self):
        super().__init__('node2')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(Float64MultiArray, '/random_array', self.array_callback, qos_profile)
        self.publisher_ = self.create_publisher(Twist, '/twist_topic', qos_profile)
        self.subscription  # prevent unused variable warning

    def array_callback(self, msg):
        twist = Twist()
        if len(msg.data) >= 2:
            twist.linear.x = msg.data[0]
            twist.angular.z = msg.data[1]
        self.publisher_.publish(twist)
        self.get_logger().info(f'Published Twist: linear.x={twist.linear.x}, angular.z={twist.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 