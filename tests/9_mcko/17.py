file = open(r"D:\Study\egeinfo\tests\9_mcko\1003_17.txt")
lines = [int(line) for line in file]
y = max([i for i in lines if abs(i) % 100 == 17])

res = []
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i]
    spl = [a, b, c]
    n1 = [x for x in spl if len(str(abs(x))) == 4]
    if len(n1) == 0 and sum(spl) > y:
        res.append(sum(spl))
print(len(res), max(res))