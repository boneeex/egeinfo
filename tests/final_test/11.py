from math import *

for n in range(1000_000, 1, -1):
    i1 = ceil(log2(26))
    ser1 = i1 * 8
    i2 = ceil(log2(n))
    ser2 = i2 * 6
    ser3 = ceil((ser1 + ser2) / 8)
    if 55 * ser3 <= 1024:
        print(n)
        break