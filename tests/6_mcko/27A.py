file = open(r"D:\Study\egeinfo\tests\6_mcko\1003_27_A.txt")

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
for star in file:
    x, y = list(map(float, star.replace(",", ".").split(" ")))
    if y < 15: cluster1.append([x, y])
    else: cluster2.append([x, y])

x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)
A2 = ((x1 - 2.1) ** 2 + (y1 + 0.7) ** 2) ** 0.5 + ((x2 - 2.1) ** 2 + (y2 + 0.7) ** 2) ** 0.5

print(abs(len(cluster1) - len(cluster2)), int(A2 * 10000))