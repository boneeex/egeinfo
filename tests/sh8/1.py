from itertools import permutations

tab = "678 34 2467 235 46 135 138 17".split(" ")
pic = "аб бг гд ди иж еж ве ав аг ге жд".split(" ")

print(*range(1, 9))
for var in permutations("абвгдежи"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(" ".join(var))