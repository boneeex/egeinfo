file = open(r"D:\Study\egeinfo\tests\3\Копия 9.csv")
from collections import Counter
res = []
cnt = 0
for line in file:
    cnt += 1
    line = list(map(int, line.split(";")))
    n0 = [i for i in line if line.count(i) != 1]
    n1 = [i for i in line if line.count(i) == 1]
    c = sorted(Counter(line).values())
    if 3 in c and 2 in c and len(c) == 4 and sum(n1) <= min(n0):
        res.append((min(n0), 10 ** 6 - cnt))

print(abs(sorted(res)[0][0]))