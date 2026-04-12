from math import *
i = ceil(log2(8192))
for n in range(10000, 1, -1):
    package = i * 1024 * 960 * n
    if package <= 400 * 1024 * 1024 * 8:
        print(n)
        break