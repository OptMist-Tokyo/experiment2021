from socket import *
import time
from LED import LED
from PUMP import PUMP
import numpy as np

class udprecv():
    def __init__(self, led1, led2, pump1, pump2):
        # 受信側
        SrcIP = ""
        SrcPort = 50007
        self.SrcAddr = (SrcIP, SrcPort)

        self.BUFSIZE = 1024
        self.udpServSock = socket(AF_INET, SOCK_DGRAM)
        self.udpServSock.bind(self.SrcAddr)

        self.led1 = LED(led1[0], led1[1], led1[2])
        self.led2 = LED(led2[0], led2[1], led2[2])

        self.pump1 = PUMP(pump1)
        self.pump2 = PUMP(pump2)

    def led(self, rgb)
        r,g,b = [int(x) for x in rgb]
        self.led1(r, g, b)
        self.led2(r, g, b)

    def pump(self, power)
        self.pump1(power)
        self.pump2(power)

    def recv(self):
        while True:
            data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
            
            cmd = data.decode()
            print(f'get "{cmd}" from {addr}')
            invalid = True
            
            if len(cmd) < 2:
                invalid = True
            elif cmd == 'stop':
                print('  stop all devices')
                self.led(0, 0, 0)
                self.pump(0)
                invalid = False
            elif cmd[0] == 'l':
                rgb = np.array([int(x) for x in (cmd.split(":")[-1]).split(",")])
                self.led(rgb)
                print(f'  set led = {rgb}')
                invalid = False
            elif cmd[0] == 'p':
                power = int(cmd.split(":")[-1])
                self.pump(power)
                print(f'  set pump0 = {power}')
                invalid = False
            if invalid:
                print('[[WARNING]] invalid command')
            
if __name__ == '__main__':
    udp = udprecv([18, 16, 25], [5, 4, 22], 19, 26)
    udp.recv()

