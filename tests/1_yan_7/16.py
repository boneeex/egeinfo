def f(n):
    res = 0
    while n > 2:
        if n % 2 == 0:
            res += n - 1
            n -= 1
        else:
            res += 2 * (n - 1)
            n -= 2
    return 1 + res

print(f(3048) - f(3045))