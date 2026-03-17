def i(a, b):
    return ~a|b

def f(a, x):
    return i(1768, x) == 0 or (not (i(1240, x) != 0) or i(305, x) == 0 or i(a, x) != 0)

for a in range(1, 1000):
    if all(f(a, x) for x in range(100000)):
        print(a)
        break

print(i(19, 7))
print(~19)