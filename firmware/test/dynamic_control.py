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
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

def setLedImpl(r, g, b):
    pi.softPwmWrite(red, int(r))
    pi.softPwmWrite(green, int(g))
    pi.softPwmWrite(blue, int(b))

def setLed(x):
    setLedImpl(100*x[0], 100*x[1], 100*x[2])

setLed([0.5, 0.5, 0.])
while True:
    T = 0.01
    n = 2
    for i in range(n):
        GPIO.output(12, GPIO.HIGH if i==0 else GPIO.LOW)
        time.sleep(T/n)

