file = open(r"D:\Study\egeinfo\tests\3\27_A.txt")

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