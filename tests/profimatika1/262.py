# https://education.yandex.ru/ege/inf/task/f702f7af-87ae-4eab-b8f7-a8a16590cbcf
file = open(r"D:\Study\egeinfo\tests\profimatika1\26 (2).txt")
# 2035 50000
workers = sorted([(int(i.split(" ")[0]), i.split(" ")[1].strip()) for i in file], key=lambda x: [x[0], -ord(x[1])])
n = 50_000
cnt = 0
last = -1
while n > workers[0][0]:
    last = workers.pop(0)
    n -= last[0]
    if last[1] == "G":
        cnt += 1
print(cnt - 1, n)    
print(len(workers))