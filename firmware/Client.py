from socket import *
import time
import sys

class udpsend():
def __init__(self, SrcPort=50002, SrcIP='127.0.0.1'):
        # 送信元
        self.SrcAddr = (SrcIP, SrcPort)

        # 送信先
        DstIP = '127.0.0.1' # ここにIPを書く
        DstPort = 50007
        self.DstAddr = (DstIP,DstPort)

        self.udpClntSock = socket(AF_INET, SOCK_DGRAM)
        self.udpClntSock.bind(self.SrcAddr)

    def send(self, cmd):
        print(f'send {cmd}')
        cmd = cmd.encode('utf-8')
        self.udpClntSock.sendto(cmd, self.DstAddr)
    
    def led(self, r, g, b):
        self.send(f'led: {r},{g},{b}')

    def pump(self, power):
        self.send(f'pump: {power}')

    def gpump(self, start, end, T):
        dt = 0.1
        n = int(T/dt)
        self.pump(start)
        for i in range(n):
            time.sleep(dt)
            power = int(start + (i+1)/n * (end-start))
            self.pump(power)

    def cpump(self, start, end, T):
        dt = 0.1
        n = int(T/dt)
        self.pump(start)
        for i in range(n):
            time.sleep(dt)
            power = int(start + (i+1)/n * (end-start))
            self.p0(power)
            self.p1(100-power)

    def stop(self):
        self.send("stop")

if __name__ == '__main__':
    send = udpsend(50002, SrcIP='172.17.0.1')
    if len(sys.argv) >= 4:
        r,g,b = [int(x) for x in sys.argv[1:4]]
        send.led(r, g, b)

