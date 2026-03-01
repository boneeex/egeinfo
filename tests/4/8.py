from itertools import product
cnt = 0
for var in product("ЖАСМИН", repeat=5):
    if var.count("Ж") >= 2:
        cnt += 1

print(cnt)