from functools import lru_cache

@lru_cache(None)
def f(a, m):
    if a >= 126:
        return m % 2 == 0
    
    if m == 0:
        return False
    
    h = [f(a + 1, m - 1), f(a + 3, m - 1), f(a * 2, m - 1)]

    if m % 2 == 1:
        return any(h)
    return all(h)

for s in range(1, 125 + 1):
    if f(s, 1) == False and f(s, 2) == True:
        print(s)
        break

res = []
for s in range(1, 125 + 1):
    if f(s, 1) == False and f(s, 3) == True:
        res.append(s)
print(*res)

for s in range(1, 125 + 1):
    if f(s, 2) == False and f(s, 4) == True:
        print(s)
        break