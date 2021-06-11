import RPi.GPIO as GPIO
import wiringpi as pi
import time
import colorsys as cs

GPIO.setmode(GPIO.BCM)
class PUMP:
    def __init__(self, pump):
        self.pump = pump
        GPIO.setup(self.pump, GPIO.OUT)

    def __call__(self, onoff):
        if bool(onoff) is True:
            GPIO.output(self.pump, GPIO.HIGH)
        else:
            GPIO.output(self.pump, GPIO.LOW)

if __name__ == '__main__':
    pump = PUMP(2)
    
    for i in range(4):
        pump(i%2)
        time.sleep(0.5)
    pump(0)
