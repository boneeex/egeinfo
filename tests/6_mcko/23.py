def f(x, y, stop):
    if x < y or x == stop:
        return 0
    if x == y:
        return 1
    
    return f(x - 3, y, stop) + f(x - 9, y, stop) + f(x // 2, y, stop)

print(f(86, 29, 77) * f(29, 13, 77))