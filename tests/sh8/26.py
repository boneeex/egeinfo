file = open(r"D:\informaticsclass\egeinfo\tests\sh8\26_2024.txt")
n = int(file.readline())
conf = sorted([list(map(int, line.split(" "))) for line in file], key=lambda x: [x[1], x[0]])
psevdo_conf = sorted(conf)
accepted = [conf.pop(0)]

for i in conf:
    start, stop = i
    if accepted[-1][1] <= start:
        accepted.append(i)

print(psevdo_conf[-1])
print(accepted)
print(len(accepted), 1288 - 1273)