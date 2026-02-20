from itertools import permutations

tab = "246 16 57 15 347 127 356".split(" ")
pic = "ef fd dc ca ag gb be ba fc".split(" ")

print(*range(1, 8))
for var in permutations("abcdefg"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))