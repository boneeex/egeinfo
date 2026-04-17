from math import *

i = ceil(log2(2 ** 23))

print(int(120 * (1920 * 1080 * i - 1280 * 1024 * 21) / 8 / 1024))