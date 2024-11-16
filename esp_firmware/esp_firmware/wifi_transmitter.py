import rclpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import socket

global node, arduino
def callback_message(msg: Twist):
    global node, arduino
    data = '0'
    if (msg.linear.x > 0):
        data = '1'
    if (msg.linear.x < 0):
        data = '2'
    if(msg.angular.z > 0):
        data = '3'
    if(msg.angular.z < 0):
        data = '4'

    arduino.send(data.encode('utf-8'))

def create_wifi(node):
    node.declare_parameter('ip', '192.168.68.108')
    node.declare_parameter('port', 8144)
    ip = node.get_parameter('ip').get_parameter_value().string_value
    port = node.get_parameter('port').get_parameter_value().integer_value
    arduino = socket.socket()
    arduino.connect((ip, port))
    return arduino

def main():
    global node, arduino
    rclpy.init()
    node = rclpy.create_node('wifi_transmitter')
    # 1 Crear el subscriber
    subs = node.create_subscription(Twist, 'wifi/transmitter', callback_message, 10)
    arduino = create_wifi(node)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
