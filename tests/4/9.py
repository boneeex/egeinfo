file = open(r"D:\Study\egeinfo\tests\4\9_10__2r78y.csv")
cnt = 0
for line in file:
    line = list(map(int, line.split(";")))
    n1 = [i for i in line if i > 100]
    n2 = [i for i in line if line.count(i) > 1]
    n3 = [i for i in line if line.count(i) == 1]
    if len(n1) and sum(n3) <= sum(n2):
        cnt += 1
print(cnt)