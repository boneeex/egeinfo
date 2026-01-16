file = open(r"D:\informaticsclass\egeinfo\27\1\27_A_23766.txt")

lines = [list(map(float, line.replace(",", ".").split(" "))) for line in file]

first_cl = []
second_cl = []

for var in lines:
    if var[1] > 8:
        second_cl.append(var)
    else:
        first_cl.append(var)


centroid = []
def centroid(claster):
    best_star = []
    sm = 10 ** 7
    for i in claster:
        cur_sm = 0
        for j in claster:
            x1, y1 = i[0], i[1]
            x2, y2 = j[0], j[1]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            cur_sm += dist
        if cur_sm < sm:
            best_star = [x1, y1]
            sm = cur_sm
    return best_star

print(centroid(first_cl))
print(centroid(second_cl))