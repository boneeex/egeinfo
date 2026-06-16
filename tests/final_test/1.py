from itertools import *

tab = "28 1348 267 26 78 34 358 1257".split(" ")
pic = "иа аб бв вг гд де еж иж бд аж жд".split(" ")

print(*range(1, 9))
for var in permutations("абвгдежи"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print("".join(var))