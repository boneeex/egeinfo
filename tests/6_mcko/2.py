print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (z <= (not (((not x) == w) and (y <= w)))):
                    print(x,y,z,w)

def check(x, y, z, w):
    return z <= (not (((not x) == w) and (y <= w)))

print(check(0, 0, 1, 1))
print(check(0, 1, 1, 1))
print(check(1, 0, 1, 0))