file = open(r"D:\Study\egeinfo\tests\6_mcko\1002_17.txt")
lines = [int(i) for i in file]
y = max([i for i in lines if abs(i) % 100 == 17])

res = []
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i]
    lst = [a, b, c]
    n1 = [i for i in lst if len(str(abs(i))) == 4]
    n2 = sum(lst) > y
    if len(n1) > 0 and n2:
        res.append(sum(lst))
print(len(res), max(res))