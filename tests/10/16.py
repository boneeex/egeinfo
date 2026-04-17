from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 5)

@lru_cache(None)
def f(n):
    if n < 10:
        return n
    else:
        return 3 * n + f(n - 3)
    
print((f(6250) + 2 * f(6244)) / f(6238))