import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from std_msgs.msg import ColorRGBA
from rpi_ws281x import Adafruit_NeoPixel, Color

# Define the number of WS2812B LED lights and the pin they are connected to
NUM_LEDS = 12  # Number of LED
LED_PIN = 18  # 0- number will form a color

class Ws2812Node(Node):

    def __init__(self):
        # Initialize the WS2812B LED lights
        strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN)
        strip.begin()
        strip.show()

        for i in range(NUM_LEDS):
            strip.setPixelColor(i, Color(int(50* 255), int(60 * 255), int(0 * 255)))
            strip.show()

        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    subscriber = Ws2812Node()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()