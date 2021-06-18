import wiringpi as pi
import time
import colorsys as cs

pi.wiringPiSetupGpio()
class PUMP:
    def __init__(self, pump):
        self.pump = pump
        pi.pinMode(self.pump, pi.OUTPUT)
        pi.softPwmCreate(self.pump, 0, 100)
        pi.softPwmWrite(self.pump, 0)

    def __call__(self, power):
        pi.softPwmWrite(self.pump, power)

if __name__ == '__main__':
    pump = PUMP(2)
    
    for i in range(4):
        for j in range(10):
            pump(10*(j+1))
            time.sleep(0.1)
    pump(0)
