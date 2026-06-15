from math import dist

def centroid(cluster):
    best_star = []
    min_dist = 10 ** 7
    for star1 in cluster:
        cur_dist = 0
        for star2 in cluster:
            x1, y1 = star1[0], star1[1]
            x2, y2 = star2[0], star2[1]
            cur_dist += dist([x1, y1], [x2, y2])
        if cur_dist <= min_dist:
            min_dist = cur_dist
            best_star = star1
    return best_star

file = open(r"D:\informaticsclass\egeinfo\27\29080\27_B_29080.txt")
cluster1 = []
cluster2 = []
cluster3 = []
for star in file:
    star = [float(star.replace(",", ".").split()[0])] + [float(star.replace(",", ".").split()[1])] + [star.split()[2]]
    if star[0] > 22: cluster1.append(star)
    elif star[0] < 22 and star[1] < 23: cluster2.append(star)
    else: cluster3.append(star)

cen1, cen2, cen3 = centroid(cluster1), centroid(cluster2), centroid(cluster3)
blue1, blue2, blue3 = len([i for i in cluster1 if i[2].startswith("L")]), len([i for i in cluster2 if i[2].startswith("L")]), len([i for i in cluster3 if i[2].startswith("L")])

res1 = dist([cen1[0], cen1[1]], [cen3[0], cen3[1]])

res2 = 0
for star1 in cluster1 + cluster2 + cluster3:
    for star2 in cluster1 + cluster2 + cluster3:
        if star1[2].startswith("L") and star2[2].startswith("L"):
            same = any([(star1 in cluster1 and star2 in cluster1),
                        (star1 in cluster2 and star2 in cluster2),
                        (star1 in cluster3 and star2 in cluster3)])
            if not same:
                res2 = max(res2, dist([star1[0], star1[1]], [star2[0], star2[1]]))

print(int(res1 * 10_000), int(res2 * 10_000))