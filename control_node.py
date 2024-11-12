# ~/4wd_robot_ws/src/four_wheel_drive/nodes/control_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class FourWheeledRobot(Node):
    def __init__(self):
        super().__init__('four_wheel_drive_controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_robot)

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.5  # Adjust this value for forward speed
        msg.angular.z = 0.0 # Adjust for turning
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FourWheeledRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
