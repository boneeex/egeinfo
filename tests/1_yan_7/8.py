from itertools import product

def check(spl):
    for i in range(1, len(spl)):
        if spl[i - 1] in "ОЕ" and spl[i] in "ОЕ":
            return False
    return True


cnt = 0
for var in product("БЛОГЕР", repeat=4):
    if check(var) and var.count("Г") == 1:
        cnt += 1
print(cnt)