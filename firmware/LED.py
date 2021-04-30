import RPi.GPIO as GPIO
import wiringpi as pi
import time
import colorsys as cs

class LED:
    def __init__(self, red, green, blue):
        self.leds = [red, green, blue]
        pi.pinMode(led, pi.OUTPUT)
        for led in leds:
            pi.softPwmCreate(led, 0, 100)
            pi.softPwmWrite(led, 0)
        GPIO.setup(12, GPIO.OUT)

    def impl(self, r, g, b):
        pi.softPwmWrite(red, int(r))
        pi.softPwmWrite(green, int(g))
        pi.softPwmWrite(blue, int(b))

    def __call__(self, r, g, b):
        # rgbをそれぞれ0.0~1.0で渡す
        self.softPwmWrite(red, 100*r, 100*g, 100*b)


if __name__ == '__main__':
    led = LED(21, 20, 16)
    led(0.5, 0.3, 0.0)
    time.sleep(1.0)

