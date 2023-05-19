#!/usr/bin/env python3
import serial
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class ArduinoTalker(Node):
    def __init__(self):
        super().__init__("ArduinoTalker")
        self.publisher_ = self.create_publisher(String, "arduino", 10)
        self.get_logger().info("Ardunio talker activated :)")
        msg = String()
        msg.data = 'm 180 180' + '\r'
        self.publisher_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = ArduinoTalker()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
