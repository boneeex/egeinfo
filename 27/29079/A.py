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

file = open(r"D:\informaticsclass\egeinfo\27\29079\27_A_29079.txt")
cluster1 = []
cluster2 = []
for star in file:
    star = [float(star.replace(",", ".").split()[0])] + [float(star.replace(",", ".").split()[1])] + [star.split()[2]]
    if star[1] < 8: cluster1.append(star)
    else: cluster2.append(star)

cen1, cen2 = centroid(cluster1), centroid(cluster2)
sub1, sub2 = [i for i in cluster1 if i[2].startswith("N") and i[2].endswith("IV")], [i for i in cluster2 if i[2].startswith("N") and i[2].endswith("IV")]

res1 = 10 ** 7
for star in sub1:
    res1 = min(res1, dist([star[0], star[1]], [cen2[0], cen2[1]]))
for star in sub2:
    res1 = min(res1, dist([star[0], star[1]], [cen1[0], cen1[1]]))

res2 = 0
for star in sub1:
    res2 = max(res1, dist([star[0], star[1]], [cen2[0], cen2[1]]))
for star in sub2:
    res2 = max(res1, dist([star[0], star[1]], [cen1[0], cen1[1]]))

print(int(res1 * 10_000), int(res2 * 10_000))