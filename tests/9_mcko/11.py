from math import *

for n in range(1, 10 ** 7):
    i = ceil(log2(n))
    ser = ceil(i * 185 / 8)
    if ser * 131072 >= 25 * 1024 * 1024:
        print(n)
        break