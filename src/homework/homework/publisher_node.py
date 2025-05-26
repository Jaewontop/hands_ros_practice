import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(Twist, '/my_topic', qos_profile)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.1
        msg.angular.z = 0.1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "linear.x: %f, angular.z: %f"' % (msg.linear.x, msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 