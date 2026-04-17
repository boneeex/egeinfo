from itertools import permutations

tab = "478 38 256 15 34 37 168 127".split(" ")
pic = "fe ed dg ga ah hf fb hb bc cg".split(" ")

print(*range(1, 9))
for var in permutations("abcdefgh"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))