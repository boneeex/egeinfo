file = open(r"D:\informaticsclass\egeinfo\tests\10\9_23193.csv")
mx = 0
cnt = 0
for line in file:
    cnt += 1
    line = list(map(int, line.split(";")))
    n1 = [i for i in line if line.count(i) == 3]
    n2 = [i for i in line if line.count(i) == 1]
    if len(set(n1)) == 1 and len(n2) == 3 and n1[0] > sum(n2) / len(n2):
        mx = max(mx, cnt)
print(mx)