file = open(r"D:\informaticsclass\egeinfo\27\18056\27A_18056.txt")
lines = [list(map(float, line.replace(",", ".").split("\t"))) for line in file]

def centroid(cluster):
    best_star = []
    sm = 10 ** 7
    for i in cluster:
        cur_sm = 0
        for j in cluster:
            x1, y1 = i[0], i[1]
            x2, y2 = j[0], j[1]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            cur_sm += dist
        if cur_sm < sm:
            best_star = [x1, y1]
            sm = cur_sm
    return best_star

cluster_1 = []
cluster_2 = []

for star in lines:
    x = star[0]
    y = star[1]
    if (x + 1) ** 2 + (y - 1.1) ** 2 <= 1:
        cluster_1.append(star)
    if (x - 1.9) ** 2 + (y + 2) ** 2 <= 1:
        cluster_2.append(star)

x1, y1 = centroid(cluster_1)[0], centroid(cluster_1)[1]
x2, y2 = centroid(cluster_2)[0], centroid(cluster_2)[1]

print((x1 + x2) / 2 * 100000, (y1 + y2) / 2 * 100000)