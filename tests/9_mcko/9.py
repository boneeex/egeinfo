file = open(r"D:\Study\egeinfo\tests\9_mcko\1002_9.csv")
cnt = 0
for line in file:
    line = list(map(int, line.split(";")))
    n1 = [i for i in line if line.count(i) == 2]
    if len(set(line)) == 5 and min(line) not in n1:
        cnt += 1
print(cnt)