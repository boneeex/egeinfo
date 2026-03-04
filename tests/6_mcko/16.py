def g(n):
    res = 0
    while n > 70:
        res += 23
        n -= 7
    return 3 * n ** 2 - n + res

def f(n):
    return 13 * g(n + 58) - 37

print(f(167_462))