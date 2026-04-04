file = open(r"D:\informaticsclass\egeinfo\27\18678\27B_18678.txt")
stars = [list(map(float, line.replace(",", ".").split())) for line in file]

def dist(star1, star2):
    x1, y1 = star1
    x2, y2 = star2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def db_scan(star1):
    x, y = star1
    cluster = []
    for star2 in stars:
        if dist(star1, star2) < 0.7:
            cluster.append(star2)
            stars.remove(star2) 
    a = [db_scan(star) for star in cluster]
    for i in a:
        cluster += i
    return cluster

def centroid(cluster):
    best_star = []
    best_dist = 10 ** 7
    for star1 in cluster:
        sm = 0
        for star2 in cluster:
            curr = dist(star1, star2)
            sm += curr
        if sm < best_dist:
            best_dist = sm
            best_star = star1
    return best_star

clusters = []
while stars:
    clusters.append(db_scan(stars[0]))
print(len(clusters))
clusters = [i for i in clusters if len(i) >= 30]
print(len(clusters))
centroids = [centroid(i) for i in clusters]
x = sum(i[0] for i in centroids) / len(centroids)
y = sum(i[1] for i in centroids) / len(centroids)
print(int(100000 * x), int(100000 * y))