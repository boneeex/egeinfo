def f(n):
    if n < 20:
        return n
    return 3 * (n - 2) * f(n - 6)

print(4 * f(873) / f(861))