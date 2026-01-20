import math
file = open(r"D:\Study\egeinfo\tests\1_yan_7\17.txt")

lines = [int(i) for i in file]
max1, max2 = sorted(lines)[-1], sorted(lines)[-2]
ans = []
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i]
    n1 = [i for i in [a, b, c] if i > 0]
    n2 = math.prod([a, b, c])
    if len(n1) == 1 and n2 <= max1 * max2:
        ans.append(a + b + c)

print(len(ans), max(ans))