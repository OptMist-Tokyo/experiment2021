import RPi.GPIO as GPIO
import wiringpi as pi
import time
import colorsys as cs

class LED:
    def __init__(self, red, green, blue):
        self.leds = [red, green, blue]
        pi.wiringPiSetupGpio()
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
    led = LED(17, 27, 22)
    led(120, 120, 120)
    time.sleep(1.0)


