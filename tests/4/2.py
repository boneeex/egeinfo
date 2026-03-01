from itertools import*
def f(w,x,y,z):
    return (w <= (y == z)) and (y == (z <= x))
for a1,a2 in product([0,1], repeat = 2):
    t = [(a1, 0, 0, 0),(0, a2, 1, 1),(0, 0, 0, 1)]
    if len(t) == len(set(t)):
        for i in permutations("wxyz"):
            if [f(**dict(zip(i, h))) for h in t] == [1,1,0]:
                print(i)
