file = open(r"D:\informaticsclass\egeinfo\27\3\dz_27_11B.txt")

lines = [list(map(float, line.replace(",", ".").split("\t"))) for line in file]

def centroid(claster):
    best_star = []
    sm = 10 ** 7
    for i in claster:
        cur_sm = 0
        for j in claster:
            x1, y1 = i[0], i[1]
            x2, y2 = j[0], j[1]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            cur_sm += dist
        if cur_sm < sm:
            best_star = [x1, y1]
            sm = cur_sm
    return best_star

claster_1 = []
claster_2 = []
claster_3 = []
for star in lines:
    x = star[0]
    y = star[1]
    if y >= -2 * x + 20:
        claster_1.append(star)
    if y <= -2 * x + 20 and y >= x + 3:
        claster_2.append(star)
    if y <= -2 * x + 20 and y <= x + 3:
        claster_3.append(star)

a = centroid(claster_1)
b = centroid(claster_2)
c = centroid(claster_3)

print((a[0] + b[0] + c[0]) / 3)
print((a[1] + b[1] + c[1]) / 3)