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

file = open(r"D:\Study\egeinfo\tests\9_mcko\1004_27_A.txt")
file = [list(map(float, line.replace(",", ".").strip().split(" "))) for line in file]

cluster1 = []
cluster2 = []
for star in file:
    x, y = star
    if y < 15:
        cluster1.append(star)
    else:
        cluster2.append(star)

x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)

print(max(len(cluster1), len(cluster2)))
print(int(10_000 * (((x1 - 0.3) ** 2 + (y1 - 0.75) ** 2)**0.5 + ((x2 - 0.3) ** 2 + (y2 - 0.75) ** 2)**0.5)))