from math import *
def f(a, b, m):
    if a + b <= 60:
        return m % 2 == 0
    
    if m == 0:
        return False
    
    h = [f(a - 5, b, m - 1), f(a, b - 3, m - 1), f(floor(a / 2), b, m - 1), f(a, ceil(b / 2), m - 1)]

    if m % 2 == 1:
        return any(h)
    return all(h)

ans = []
# В начальный момент в первой куче было сто тридцать  камней, во второй куче – S камней; 5 ≤ S ≤ 150.
for s in range(5, 151):
    if f(130, s, 1) == False and f(130, s, 3) == False and f(130, s, 5) == True:
        ans.append(s)

print(prod(ans))