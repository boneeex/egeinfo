from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

@lru_cache(None)
def f(x, y, destination, magic_cnt, visited=False):
    if (x, y) == destination and visited:
        return 1
    if [x, y] == [30, 33]:
        visited = True
    if (x + y) % 2 == 0:
        magic_cnt += 1
    if magic_cnt > 4 or x > 70 or y > 70:
        return 0

    return f(x + 1, y,         destination, magic_cnt, visited) +\
           f(x,     y + 1,     destination, magic_cnt, visited) +\
           f(x + 1, y + 1,     destination, magic_cnt, visited)

print(f(2, 5, (70, 70), 0))