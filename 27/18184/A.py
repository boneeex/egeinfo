# 2
# 1 1 2
# 20 20 3
import math
def centroid(cluster, x_center, y_center, radius):
    sm_dist = 0
    cnt = 0
    for star in cluster:
        x = star[0]
        star = star[1]
        d = math.hypot(x - x_center, y - y_center) - radius
        sm_dist += d
        cnt += 1
    return int(sm_dist / cnt * 1000)

file = open(r"D:\informaticsclass\egeinfo\27\18055\27A_18055.txt")
sky = [list(map(float, line.replace(",", ".").split("\t"))) for line in file]

cluster1 = []
cluster2 = []

for star in sky:
    x = star[0]
    y = star[1]
    if 2 <= ((x - 1) ** 2 + (y - 1) ** 2) ** 0.5 <= 6:
        cluster1.append(star)
    if 3 <= ((x - 20) ** 2 + (y - 20) ** 2) ** 0.5 <= 9:
        cluster2.append(star)

print(centroid(cluster1, 1, 1, 2), centroid(cluster2, 20, 20, 3))