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

    def __call__(self, r, g, b):
        # rgbをそれぞれ0.0~1.0で渡す
        self.impl([100*r, 100*g, 100*b])


if __name__ == '__main__':
    led = LED(21, 26, 16)
    led(0.5, 0.3, 0.0)
    time.sleep(1.0)

