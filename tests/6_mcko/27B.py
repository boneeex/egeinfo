file = open(r"D:\Study\egeinfo\tests\6_mcko\1003_27_B.txt")

def centroid(cluster):
    best_dist = 10 ** 7
    best_star = []
    for star1 in cluster:
        curr = 0
        for star2 in cluster:
            x1, y1 = star1
            x2, y2 = star2
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            curr += dist
        if best_dist > curr:
            best_dist = curr
            best_star = star1
    return best_star

cluster1 = []
cluster2 = []
cluster3 = []
for star in file:
    x, y = list(map(float, star.replace(",", ".").split(" ")))
    if y > 23:
        cluster1.append([x, y])
    if y < 23 and x < 24:
        cluster2.append([x, y])
    if x > 25:
        cluster3.append([x, y])

cent2 = centroid(cluster2)
cnt2 = 0
for star in cluster2:
    x, y = star
    xx, yy = cent2
    dist = ((x - xx) ** 2 + (y - yy) ** 2) ** 0.5
    if dist <= 0.9:
        cnt2 += 1

cent3 = centroid(cluster3)
cnt3 = 0
mn = 10 ** 7
for star in cluster3:
    x, y = star
    xx, yy = cent3
    dist = ((x - xx) ** 2 + (y - yy) ** 2) ** 0.5
    if dist != 0:
        mn = min(mn, dist)
print(cnt2, int(mn * 10000))
