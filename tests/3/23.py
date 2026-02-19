from functools import lru_cache

@lru_cache(None)
def f(start, stop, zapret=None):
    if start == stop:
        return 1
    if start > stop or start in [17, 28, zapret]:
        return 0
    
    return f(start + 2, stop, zapret) + f(start + 3, stop, zapret) + f(start * 2, stop, zapret)

print(f(8, 14) * f(14, 48, 18) + f(8, 18, 14) * f(18, 48))