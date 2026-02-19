file = open(r"D:\Study\egeinfo\tests\3\17.txt")
lines = [int(line) for line in file]
y = max([i for i in lines if abs(i) % 100 == 70])

ans = []
for i in range(2, len(lines)):
    a = lines[i - 2]
    b = lines[i - 1]
    c = lines[i - 0]
    if a >= 0 and b >= 0 and c >= 0 and a + b + c <= y:
        ans.append(a + b + c)
    
print(len(ans), max(ans))