from itertools import permutations

tab = "367 345 125 26 23 147 16".split(" ")
pic = "гб ге бе еж жд дв вж ва аб".split(" ")

print(*range(1, 8))
for var in permutations("абвгдеж"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))