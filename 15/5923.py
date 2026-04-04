p = range(5, 280 + 1)
q = range(295, 400 + 1)
r = range(375, 450 + 1)
# ((x∈Q)→(x∈P))∨(¬(x∈A)→(x∈R))
for x in range(-10000, 10000):
    x = x * 0.25
    a = not (x in q) or (x in p)
    b = x in r
    if not (a or b):
        print(x)