file = open(r"D:\Study\egeinfo\tests\6_mcko\1004_9.csv")
cnt = 0
for line in file:
    line = list(map(int, line.split(";")))
    n1 = [i for i in line if line.count(i) == 3]
    n2 = [i for i in line if line.count(i) == 2]
    n3 = [i for i in line if line.count(i) == 1]
    if len(n1) == 3 and len(n2) == 2 and len(n3) == 1 and max(line) == n3[0]:
        cnt += 1
print(cnt)