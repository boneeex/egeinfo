def centroid(cluster):
    best_star = []
    best_dist = 10 ** 7
    for star1 in cluster:
        sm = 0
        for star2 in cluster:
            x1, y1 = star1
            x2, y2 = star2
            curr_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) * 0.5
            sm += curr_dist
        if sm < best_dist:
            best_dist = sm
            best_star = star1
    return best_star

file = open(r"D:\Study\egeinfo\tests\9_mcko\1004_27_B.txt")
file = [list(map(float, line.replace(",", ".").strip().split(" "))) for line in file]

cluster1 = []
cluster2 = []
cluster3 = []
for star in file:
    x, y = star
    if y > 23:
        cluster1.append(star)
    if y < 23 and x < 25:
        cluster2.append(star)
    if x > 25:
        cluster3.append(star)

c1, c2, c3 = len(cluster1), len(cluster2), len(cluster3)
x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)
x3, y3 = centroid(cluster3)

n1 = 0
for star in cluster2:
    x, y = star
    dist = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    if dist <= 1.5:
        n1 += 1

n2 = 10 ** 7
for star in cluster1:
    x, y = star
    dist = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    if dist != 0:
        n2 = min(n2, dist)

print(n1, int(n2 * 10_000))