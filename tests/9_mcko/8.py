from itertools import product

cnt = 0
glas = "аео"
sogl = "бвг"
for var in product("абвгео", repeat=7):
    gl = [i for i in var if i in glas]
    sg = [i for i in var if i in sogl]
    if len(gl) > len(sg):
        cnt += 1
print(cnt)