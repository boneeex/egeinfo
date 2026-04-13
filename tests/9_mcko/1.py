from itertools import permutations

tab = "468 347 258 128 367 15 25 134".split(" ")
pic = "ea eh hg gc cf fa fd de db bh bg".split(" ")

print(*range(1, 9))
for var in permutations("abcdefgh"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))