def f(x, y, stop):
    if x == y:
        return 1
    if x > y or x in stop:
        return 0
    
    return f(x + 3, y, stop) + f(x + 7, y, stop) + f(x * 2, y, stop)

print(f(7, 52, [16, 46]) * f(52, 61, [16, 46]) * f(61, 75, [16, 46]))