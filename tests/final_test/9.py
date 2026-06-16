file = open(r"D:\Study\egeinfo\tests\final_test\09__ant1k.csv")
cnt = 0
for line in file:
    line = list(map(int, line.split(";")))
    n1 = len(line) == len(set(line))
    n2 = len([i for i in line if i % 2 == 0]) > len([i for i in line if i % 2 == 1])
    n3 = sum([i for i in line if i % 2 == 0]) < sum([i for i in line if i % 2 == 1])
    if all([n1, n2, n3]):
        cnt += 1
print(cnt)