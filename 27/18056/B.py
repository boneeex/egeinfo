file = open(r"D:\informaticsclass\egeinfo\27\18056\27B_18056.txt")
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
cluster_3 = []

for star in lines:
    x = star[0]
    y = star[1]
    if y <= -x + 3.5 and -2 < y < 4:
        cluster_1.append(star)
    if y <= -x + 3.5 and y <= 2 * x - 2 and x > 0:
        cluster_2.append(star)
    if y >= -x + 3.5 and 0 < x < 4:
        cluster_3.append(star)

x1, y1 = centroid(cluster_1)[0], centroid(cluster_1)[1]
x2, y2 = centroid(cluster_2)[0], centroid(cluster_2)[1]
x3, y3 = centroid(cluster_3)[0], centroid(cluster_3)[1]
print(int((x1 + x2 + x3) / 3 * 100000), int((y1 + y2 + y3) / 3 * 100000))