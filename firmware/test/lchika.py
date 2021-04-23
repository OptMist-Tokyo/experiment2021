import RPi.GPIO as GPIO
import time

red = 21
green = 20
blue = 16

leds = [red, green, blue]

GPIO.setmode(GPIO.BCM)
for led in leds:
    GPIO.setup(led, GPIO.OUT)

def setGPIO(pin_num, tf):
    out = GPIO.HIGH if tf else GPIO.LOW
    GPIO.output(pin_num, out)


def setLed(r,g,b):
    setGPIO(red, r)
    setGPIO(green, g)
    setGPIO(blue, b)

while(True):
    setLed(1,0,0)
    time.sleep(0.4)
    setLed(0,1,0)
    time.sleep(0.4)
    setLed(0,0,1)
    time.sleep(0.4)


