from itertools import *

def f(x, y, z, w):
    return (x <= y) and z and (not w)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [
        (0, 1, a1, a2),
        (1, 1, a3, a4),
        (1, a5, 1, a6)
    ]
    if len(t) == len(set(t)):
        for i in permutations("xyzw"):
            if [f(**dict(zip(i, h))) for h in t] == [1, 1, 1]:
                print(i)