from itertools import permutations

tab = "346 45 16 125 247 137 56".split(" ")
pic = "ge ec cb ba af fd dg de ac".split(' ')

print(*range(1, 8))
for var in permutations("abcdefg"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))

print(7 + 11)