import wiringpi as pi
import time
import colorsys as cs

pi.wiringPiSetupGpio()
class LED:
    def __init__(self, red, green, blue):
        self.leds = [red, green, blue]
        for led in self.leds:
            pi.pinMode(led, pi.OUTPUT)
            pi.softPwmCreate(led, 0, 100)
            pi.softPwmWrite(led, 0)

    def impl(self, rgb):
        for (led, pulse) in zip(self.leds, rgb):
            pi.softPwmWrite(led, int(pulse))

    def setRGB(self, rgb):
        self(rgb[0], rgb[1], rgb[2])

    def __call__(self, r, g, b):
        # rgbをそれぞれ0~255までで表す
        self.impl([(100*ratio/255) for ratio in [r,g,b]])


if __name__ == '__main__':
    led = LED(5, 4, 22)
    while True:
        led(100, 0, 0)
        time.sleep(1.0)
        led(0, 100, 0)
        time.sleep(1.0)
        led(0, 0, 100)
        time.sleep(1.0)
        led(0, 0, 0)
        time.sleep(1.0)
