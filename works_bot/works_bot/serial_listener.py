#!/usr/bin/env python3
import serial
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class ArduinoListener(Node):
    def __init__(self):
        super().__init__("ArduinoListener")
        self._arduino = serial.Serial('/dev/ttyACM0', 9600)
        #Creamos subscripcion, recibimos los datos y los metemos en una funcion
        self.subscriber_ = self.create_subscription(
            String, "arduino", self.callback_robot_news, 10)
        self.get_logger().info("Arduino Listener activated")

    #Funcion para usar los datos recibidos
    def callback_robot_news(self, msg):
        _msg = msg.data
        self.get_logger().info(msg.data)
        self._arduino.write(_msg.encode())
        self._arduino.close()


def main(args=None):
    rclpy.init(args=args)
    node = ArduinoListener()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
