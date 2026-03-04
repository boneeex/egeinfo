from math import *

for alp in range(1, 10 ** 5):
    i = ceil(log2(alp))
    ser = ceil(145 * i / 8)
    if 131_072 * ser >= 22 * 1024 * 1024:
        print(alp)
        break