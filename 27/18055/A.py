def centroid(claster):
    best_price = 10 ** 7
    best_star = []
    for star in claster:
        x1 = star[0]
        y1 = star[1]
        sm_price = 0
        for i in claster:
            x2 = i[0]
            y2 = i[1]
            h = i[2]
            cur_price = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * h
            sm_price += cur_price
        if sm_price < best_price:
            best_price = sm_price
            best_star = star
    return best_star

cl1 = []
cl2 = []

file = open(r"D:\informaticsclass\egeinfo\27\18055\27A_18055.txt")
sky = [list(map(float, line.replace(",", ".").split("\t"))) for line in file]

for star in sky:
    if star[0] < 180:
        cl1.append(star)
    if star[0] > 340:
        cl2.append(star)

x1, x2 = centroid(cl1)[0], centroid(cl2)[0]
y1, y2 = centroid(cl1)[1], centroid(cl2)[1]

print(int((x1 + x2) / 2 * 100000), int((y1 + y2) / 2 * 100000))

