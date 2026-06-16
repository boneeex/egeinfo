from functools import lru_cache

@lru_cache()
def f(n):
    if n >= 14:
        return n  * f(n - 1)
    else:
        return 8 * g(n - 3)

@lru_cache()
def g(n):
    if n < 31:
        return 4
    else:
        return n // 2 * g(n - 2)

for i in range(641450):
    g(i)

for i in range(320726):
    f(i)

print(f(320726) // g(641450))