from math import *

for ln in range(1, 10 ** 6):
    i = ceil(log2(26 + 10 + 14170))
    ser = ceil(ln * i / 8)
    if ser * 156_314 >= 16 * 1024 ** 2:
        print(ln)
        break