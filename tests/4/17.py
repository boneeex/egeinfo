file = open(r"D:\Study\egeinfo\tests\4\4__1vf58.txt")
res = []
lines = [int(i) for i in file]
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i - 0]
    lst = [a, b, c]
    n1 = [i for i in lst if i % 10 == 3 or i % 10 == 7]
    n2 = sum(lst) < max(lines) + min(lines)
    if n1 and n2:
        res.append(sum(lst))
print(len(res), max(res))