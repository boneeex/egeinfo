from itertools import *

def f(x, y, z, w):
    return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))

for a1, a2, a3, a4 in product([0,1], repeat=4):
    t = [(a1, 1, 0, a2), (0, 1, 0, 1), (a3, 1, 0, a4)]
    if len(t) == len(set(t)):
        for i in permutations("xyzw"):
            if [f(**dict(zip(i, h))) for h in t] == [0, 0, 0]:
                print(i)