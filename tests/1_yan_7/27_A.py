file = open(r"D:\Study\egeinfo\tests\1_yan_7\27_1_A__51u7z.txt")

lines = [list(map(float, line.split(" "))) for line in file]

inner = []
outer = []
for star in lines:
    x, y = star[0], star[1]
    if y ** 2 <= 1.5 ** 2 - x ** 2:
        inner.append(star)
    else:
        outer.append(star)

    