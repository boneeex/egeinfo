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

file = open(r"D:\Study\egeinfo\tests\final_test\27_5B__achna (1).txt")
next(file)                          # пропускаем заголовок "X Y C"
cluster1 = []; cluster2 = []; cluster3 = []; cluster4 = []
for star in file:
    star = [float(star.replace(",", ".").split(" ")[0])] + [float(star.replace(",", ".").split(" ")[1])] + [star.strip().split(" ")[2]]
    x, y = star[0], star[1]
    if y < 0: cluster1.append(star)
    elif x < -2: cluster2.append(star)
    elif x < 14: cluster3.append(star)
    else: cluster4.append(star)

cens = [centroid(cluster1), centroid(cluster2), centroid(cluster3), centroid(cluster4)]

# B1: жёлто-белые (F) карлики (I), не дальше 0,5 от антицентра своего кластера
res1 = 0
for cluster, cen in zip([cluster1, cluster2, cluster3, cluster4], cens):
    for s in cluster:
        if s[2][0] == "F" and s[2][2:] == "I" and dist([s[0], s[1]], [cen[0], cen[1]]) <= 0.5:
            res1 += 1

# B2: число кластеров, где карликов (I) больше гигантов (III)
res2 = 0
for cluster in [cluster1, cluster2, cluster3, cluster4]:
    dwarfs = sum(1 for s in cluster if s[2][2:] == "I")
    giants = sum(1 for s in cluster if s[2][2:] == "III")
    if dwarfs > giants:
        res2 += 1

print(res1, res2)