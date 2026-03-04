file = open(r"D:\informaticsclass\egeinfo\tests\5\27A_24208.txt")
cluster1 = []
cluster2 = []
for star in file:
    x, y = float(star.split(" ")[0].replace(",", ".")), float(star.split(" ")[1].replace(",", "."))
    if x > 0:
        cluster2.append([x, y])
    else:
        cluster1.append([x, y])

def find_centroid(cluster):
    best_star = []
    best_dist = 10 ** 7
    curr_dist = 0
    for star1 in cluster:
        for star2 in cluster:
            x1, y1 = star1
            x2, y2 = star2
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            curr_dist += dist
        if best_dist > curr_dist:
            best_star = star1
            best_dist = curr_dist
        curr_dist = 0
    return best_star

x1, y1 = find_centroid(cluster1)
x2, y2 = find_centroid(cluster2)
print(int(abs(x1 + x2) * 10 ** 4), int(abs(y1 + y2) * 10 ** 4))