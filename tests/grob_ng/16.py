import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 10:
        return n
    if n % 2 == 0:
        return f(n - 1) 
    else:
        return f(n - 1) + 2

print(f(4567))