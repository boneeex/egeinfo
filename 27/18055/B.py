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
cl3 = []

file = open(r"D:\informaticsclass\egeinfo\27\18055\27B_18055.txt")
sky = [list(map(float, line.replace(",", ".").split("\t"))) for line in file]

for star in sky:
    x = star[0]
    y = star[1]
    if y < -30 and x < 0:
        cl1.append(star)
    if y > -10 and y < 120 and x > -110 and x < 10:
        cl2.append(star)
    if x > 90 and x < 210:
        cl3.append(star)

x1, x2, x3 = centroid(cl1)[0], centroid(cl2)[0], centroid(cl3)[0]
y1, y2, y3 = centroid(cl1)[1], centroid(cl2)[1], centroid(cl3)[1]
print(abs(int((x1 + x2 + x3) * 100000 / 3) ), abs( int((y1 + y2 + y3) * 100000 / 3)) )