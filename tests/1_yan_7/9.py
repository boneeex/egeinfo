file = open(r"D:\Study\egeinfo\tests\1_yan_7\9.csv")
cnt = 0
for line in file:
    line = list(map(int, line.split(";")))
    n1 = [i for i in line if line.count(i) == 2]
    n1 = set(n1)
    n2 = [i for i in line if line.count(i) == 1]
    if len(n1) == 3 and n2[0] not in [max(line), min(line)]:
        cnt += 1
print(cnt)