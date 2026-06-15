from math import dist
file = open(r"D:\informaticsclass\egeinfo\27\29357\27_A_29357.txt")
# 5,384507 8,788353 F6II
cluster1 = []
cluster2 = []
for star in file:
    x, y, types = star.replace(",", ".").split()
    x, y = float(x), float(y)
    new_star = [x, y, types]
    if y < 15: cluster1.append(new_star)
    else: cluster2.append(new_star)

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

cent1 = centroid(cluster1)
res = []
for star in cluster1 + cluster2:
    if star[-1].endswith("III") and star[-1].startswith("M"):
        res.append((dist([star[0], star[1]], [cent1[0], cent1[1]]), star))

res1, res2 = min(res)[-1][0], min(res)[-1][1]
print(int(res1 * 10_000), int(res2 * 10_000))