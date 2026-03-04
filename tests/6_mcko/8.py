from itertools import product

alp = "АБВГДЕИО"
glas = 'АЕИО'
sogl = "БВГД"

o = 0
cnt = 0
for var in product(alp, repeat=6):
    o += 1
    gl = [i for i in var if i in glas]
    so = [i for i in var if i in sogl]
    if len(gl) > len(so):
        cnt += 1
print(cnt)
