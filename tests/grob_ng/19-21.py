from math import *
def f(a, m, move="santa"):
    if a >= 50 and a <= 87:
        return m % 2 == 0
    elif a > 87:
        return m % 2 == 1

    if m == 0:
        return False

    if move == "santa":
        h = [f(a + 1, m - 1, "snow"), f(a + 3, m - 1, "snow")] + [f(ceil(a * 2.5), m - 1, "snow")]
    else:
        h = [f(a + 1, m - 1), f(a + 3, m - 1), f(floor(a * 2.5), m - 1)]
    
    if m % 2 == 1:
        return any(h)
    return all(h)

for s in range(1, 51):
    if f(s, 2) == True:
        print(s)
        break

cnt = 0
for s in range(1, 51):
    if f(s, 1) == False and f(s, 3) == True:
        cnt += 1
print(cnt)

res = []
for s in range(1, 51):
    if f(s, 8) == True and f(s, 2) == False:
        res.append(s)
print(min(res), max(res))
