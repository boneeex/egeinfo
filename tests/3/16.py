from functools import lru_cache

@lru_cache(None)
def g(n):
    res = 0
    while n < 384242:
        res += 12
        n += 41
    return res + 18 + n // 4

@lru_cache(None)
def f(n):
    res = 0
    while n >= 20:
        res += 4620
        n -= 4
    return 8 * (g(n - 12) - 21)

print(f(913))