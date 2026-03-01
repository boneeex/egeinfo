from math import *

for dop in range(1, 1000):
    i = ceil(log2(25 * 2))
    n = ceil(i * 11 / 8)
    n = n + dop
    if 12 * n == 156:
        print(dop)
        break
