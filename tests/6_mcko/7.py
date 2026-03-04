from math import *
for cnt in range(500, 1, -1):
    i = ceil(log2(2048))
    photo = 1280 * 960 * i
    if cnt * photo <= 600 * 1024 * 1024 * 8:
        print(cnt)
        break