from math import *
for n in range(1, 10 ** 6):
    i = ceil(log2(n))
    ser = ceil(i * 172 / 8)
    if 356_984 * ser >= 54 * 1024 ** 2:
        print(n)
        break