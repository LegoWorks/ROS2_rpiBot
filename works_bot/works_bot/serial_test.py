#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import serial
import time


class Arduino(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("Arduino") # MODIFY NAME
        self.get_logger().info("Sending command to Ardunio")
        self._arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(0.5)
        msg = 'm 180 180' + '\r'
        self._arduino.write(msg.encode())
        self._arduino.close()


def main(args=None):
    rclpy.init(args=args)
    node = Arduino() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
