from itertools import permutations

tab = "45 345 256 127 123 37 46".split(" ")
pic = "gf bf bd de ea ag cg cd cb".split(" ")

print(*range(1, 8))
for var in permutations("abcdefg"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))