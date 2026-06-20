file = open(r"D:\Study\egeinfo\tests\final_test\26_4__94fik.txt")
n, k = list(map(int, file.readline().split()))
areas = sorted([int(file.readline()) for i in range(n)], reverse=True)
# power price
machines = sorted([list(map(int, file.readline().split())) for i in range(k)], key=lambda x: [x[1], -x[0]])
res1 = 0
res2 = 10 ** 7
for area in areas:
    for machine in machines:
        if machine[0] >= area:
            res1 += machine[1]
            res2 = min(res2, machine[0])
            break
print(res1, res2)