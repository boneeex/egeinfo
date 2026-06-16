file = open(r"D:\Study\egeinfo\tests\final_test\17__8syxa.txt")
lines = [int(i) for i in file]
y = len([i for i in lines if len(str(abs(i))) == 5 and abs(i) % 10 == 7]) ** 2
res = []
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i - 0]
    lst = sorted([a, b, c])
    if lst[1] ** 2 + lst[2] ** 2 < y:
        res.append(sum(lst))
print(len(res), abs(max(res)))