from itertools import permutations

tab = "348 67 156 18 367 235 258 147".split(" ")
pic = "bd dg ga af fh hc cb be ed eh gf".split(" ")

print(*range(1, 9))
for var in permutations("abcdefgh"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))