from math import dist
def centroid(cluster):
    best_star = []
    best_dist = 0
    for star1 in cluster:
        cur_dist = 0
        for star2 in cluster:
            x1, y1 = star1[0], star1[1]
            x2, y2 = star2[0], star2[1]
            cur_dist += dist([x1, y1], [x2, y2])
        if cur_dist > best_dist:
            best_dist = cur_dist
            best_star = star1
    return best_star

file = open(r"D:\Study\egeinfo\tests\final_test\27_5A__achn9.txt")
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
for star in file:
    star = [float(star.replace(",", ".").split(" ")[0])] + [float(star.replace(",", ".").split(" ")[1])] + [star.strip().split(" ")[2]]
    x, y = star[0], star[1]
    if x < 3 and y < -2: cluster1.append(star)
    elif x > 3 and y < -2: cluster2.append(star)
    elif x > 3 and y > 0: cluster3.append(star)
    else: cluster4.append(star)

cen1, cen2, cen3, cen4 = centroid(cluster1), centroid(cluster2), centroid(cluster3), centroid(cluster4)

res1 = 0
for cluster in [cluster1, cluster2, cluster3, cluster4]:
    for star1 in cluster:
        for star2 in cluster:
            if star1[2][1] == "9" and star2[2][1] == "9":
                res1 = max(res1, dist([star1[0], star1[1]], [star2[0], star2[1]]))

shnurok1 = [cen1[0], cen2[0], cen3[0], cen4[0], cen1[0]]
shnurok2 = [cen1[1], cen2[1], cen3[1], cen4[1], cen1[1]]
p = sum([shnurok1[i] * shnurok2[i + 1] for i in range(4)])
q = sum([shnurok2[i] * shnurok1[i + 1] for i in range(4)])
res2 = abs(p - q) * 0.5

print(int(res1 * 10_000), int(res2 * 10_000))