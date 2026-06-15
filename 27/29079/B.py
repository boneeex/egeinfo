from math import dist

def centroid(cluster):
    best_star = []
    best_dist = 10 ** 7
    for star1 in cluster:
        cur_dist = 0
        for star2 in cluster:
            x1, y1 = star1[0], star1[1]
            x2, y2 = star2[0], star2[1]
            cur_dist += dist([x1, y1], [x2, y2])
        if cur_dist < best_dist:
            best_dist = cur_dist
            best_star = star1
    return best_star

file = open(r"D:\informaticsclass\egeinfo\27\29079\27_B_29079.txt")
cluster1 = []
cluster2 = []
cluster3 = []
for star in file:
    star = [float(star.replace(",", ".").split()[0])] + [float(star.replace(",", ".").split()[1])] + [star.split()[2]]
    if star[0] > 22: cluster1.append(star)
    elif star[0] < 22 and star[1] < 23: cluster2.append(star)
    else: cluster3.append(star)

cen1, cen2, cen3 = centroid(cluster1), centroid(cluster2), centroid(cluster3)
print(len(cluster1), len(cluster2), len(cluster3))

res1 = 0
for star in cluster1:
    if star[2].startswith("J") and star[2].endswith("V") and len(star[2]) == 3:
        res1 = max(res1, star[0])

res2 = 0
for star in cluster3:
    if star[2].startswith("J") and star[2].endswith("V") and len(star[2]) == 3:
        res2 = max(res2, star[1])

print(int(res1 * 10_000), int(res2 * 10_000))