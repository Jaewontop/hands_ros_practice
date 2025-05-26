import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(
            Twist,
            '/my_topic',
            self.listener_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received: "linear.x: %f, angular.z: %f"' % (msg.linear.x, msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 