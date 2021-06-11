from socket import *

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

    def stop(self):
        self.send("stop")

if __name__ == '__main__':
    send = udpsend(50002)


