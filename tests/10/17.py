file = open(r"D:\informaticsclass\egeinfo\tests\10\17_23201.txt")
lst = [int(i) for i in file]
y = min([i for i in lst if len(str(abs(i))) == 3 and abs(i) % 10 == 7])
res = []
for i in range(1, len(lst)):
    a = lst[i - 1]
    b = lst[i - 0]
    if (len(str(abs(a))) == 3) != (len(str(abs(b))) == 3) and (a + b) % y == 0:
        res.append(a + b)
print(len(res), min(res))