from math import dist
file = open(r"D:\informaticsclass\egeinfo\27\29357\27_B_29357.txt")
# 5,384507 8,788353 F6II
cluster1 = []
cluster2 = []
cluster3 = []
for star in file:
    x, y, types = star.replace(",", ".").split()
    x, y = float(x), float(y)
    new_star = [x, y, types]
    if y < 30: cluster1.append(new_star)
    elif y > 30 and x < 16: cluster2.append(new_star)
    else: cluster3.append(new_star)

def centroid(cluster):
    mn = 10 ** 7
    best_star = []
    for star1 in cluster:
        x1, y1, type1, = star1
        sm = 0
        for star2 in cluster:
            x2, y2, type2, = star2
            cur_dist = dist([x1, y1], [x2, y2])
            sm += cur_dist
        if sm <= mn:
            mn = sm
            best_star = star1
    return best_star

# orange1 = len([i for i in cluster1 if i[-1].startswith("K") and i[-1].endswith("III")])
# orange2 = len([i for i in cluster2 if i[-1].startswith("K") and i[-1].endswith("III")])
# orange3 = len([i for i in cluster3 if i[-1].startswith("K") and i[-1].endswith("III")])

cent1 = centroid(cluster1)
cent2 = centroid(cluster2)
cent3 = centroid(cluster3)
res1 = dist([cent1[0], cent1[1]], [cent3[0], cent3[1]])

res2 = []
for star1 in cluster1:
    if not(star1[-1].startswith("G") and star1[-1].endswith("V") and len(star1[-1]) == 3):
        continue
    for star2 in cluster1:
        if not(star2[-1].startswith("G") and star2[-1].endswith("V") and len(star2[-1]) == 3) or star1 == star2:
            continue
        res2.append(dist([star1[0], star1[1]], [star2[0], star2[1]]))

print(int(res1 * 10_000), int(max(res2) * 10_000))