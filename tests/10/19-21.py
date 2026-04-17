from math import floor
def f(a, m):
    if a <= 11:
        return m % 2 == 0
    
    h = [f(a - 3, m - 1), f(a - 7, m - 1), f(floor(a / 3), m - 1)]

    if m == 0:
        return False
    
    if m % 2 == 1:
        return any(h)
    return all(h)

for s in range(12, 100):
    if f(s, 2) == True:
        print(s)
        break

res = []
for s in range(12, 50):
    if f(s, 1) == False and f(s, 3) == True:
        res.append(s)
print(*res[:2])

for s in range(12, 50):
    if f(s, 2) == False and f(s, 4) == True:
        print(s)
        break