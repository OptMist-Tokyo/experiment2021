import sys
import pathlib
firmware_path = str(pathlib.Path('../firmware').resolve())
sys.path.append(firmware_path)

import colorsys as cs
import time

from LED import LED

if __name__ == '__main__':
    led1 = LED(17, 27, 22)
    led1(255, 255, 255)
    time.sleep(1.0)

    while True:
        N = 60
        T = 1.0
        for i in range(N):
            led1.setRGB([255*x for x in cs.hsv_to_rgb(i/N, 0.5, 0.3)])
            time.sleep(T/N)

