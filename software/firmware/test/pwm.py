import RPi.GPIO as GPIO
import wiringpi as pi
import time
import colorsys as cs

red = 21
green = 20
blue = 16

leds = [red, green, blue]

pi.wiringPiSetupGpio()
for led in leds:
    pi.pinMode(led, pi.OUTPUT)
    pi.softPwmCreate(led, 0, 100)
    pi.softPwmWrite(led, 0)
GPIO.setup(12, GPIO.OUT)

def setLedImpl(r, g, b):
    pi.softPwmWrite(red, int(r))
    pi.softPwmWrite(green, int(g))
    pi.softPwmWrite(blue, int(b))

def setLed(x):
    setLedImpl(100*x[0], 100*x[1], 100*x[2])

while True:
    T = 1.0
    n = 60
    for i in range(n):
        setLed(cs.hsv_to_rgb(i/n, 0.5, 0.3))
        time.sleep(T/n)
        GPIO.output(12, GPIO.HIGH if (i%2)==0 else GIPO.LOW)

