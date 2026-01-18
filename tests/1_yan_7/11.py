from math import *

for plus_byte in range(10 ** 6, 1, -1):
    i = ceil(log2(10 + 26 + 16_350))
    ser = ceil(i * 318 / 8)
    detail = ser + plus_byte
    if 510 * detail <= 315 * 1024:
        print(plus_byte)
        break