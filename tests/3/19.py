import math
def f(a, m):
    if a <= 1207:
        return m % 2 == 0
    
    if m == 0:
        return False
    
    h = [f(a - 3, m - 1), f(a - 5, m - 1), f(math.floor(a / 4), m - 1)]

    if m % 2 == 1:
        return any(h)
    return all(h)

for s in range(1208, 10 ** 6):
    if f(s, 1) == False and f(s, 2) == True:
        print(s)
        break