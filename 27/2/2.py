# Минимальным (максимальным) расстоянием между двумя кластерами назовём 
# минимальное (максимальное) расстояние между точками первого и второго кластера.
# Требуется найти два кластера с минимальным расстоянием 
# и вывести среднюю абсциссу и среднюю ординату двух точек, 
# на которых этот минимум достигается, 
# умножив их на 10000 и взяв целую часть 

# файлы 27_10A.txt 27_10B.txt

def dist(claster1, claster2):
    min_dist = 10 ** 6
    best_pair = []
    for star1 in claster1:
        for star2 in claster2:
            cur_dist = ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5
        if cur_dist < min_dist:
            min_dist = cur_dist
            best_pair = [cur_dist, (star1[0] + star2[0]) / 2, (star1[1] + star2[1]) / 2]
    return best_pair

file = open(r"D:\informaticsclass\egeinfo\27\2\27_10B.txt")

lines = [list(map(float, line.replace(",", ".").split(" "))) for line in file]

claster_2 = []
claster_3 = []
claster_4 = []
claster_5 = []

for star in lines:
    x = star[0]
    y = star[1]
    if x < 7 and y < 4:
        claster_2.append(star)
    if 6 <= y <= 9:
        claster_3.append(star)
    if 10 < y < 13:
        claster_4.append(star)
    if y > 14:
        claster_5.append(star)

best_dist = 10 ** 7

print(dist(claster_2, claster_3))
print(dist(claster_3, claster_4))
print(dist(claster_4, claster_5))