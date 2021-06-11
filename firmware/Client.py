from socket import *

class udpsend():
    def __init__(self, SrcPort=50002):
        # 送信元
        SrcIP = '127.0.0.1' # ここにIPを書く
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
    
    def l0(self, r, g, b):
        self.send(f'l0: {r},{g},{b}')

    def l1(self, r, g, b):
        self.send(f'l1: {r},{g},{b}')

    def led(self, rgb):
        r,g,b = rgb
        self.l0(r,g,b)
        self.l1(r,g,b)

    def p0(self, power):
        self.send(f'p0: {power}')

    def p1(self, power):
        self.send(f'p1: {power}')

    def pump(self, power):
        self.p0(power)
        self.p1(power)

    def stop(self):
        self.send("stop")

if __name__ == '__main__':
    send = udpsend(50002)


