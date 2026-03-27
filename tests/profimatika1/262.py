# https://education.yandex.ru/ege/inf/task/f702f7af-87ae-4eab-b8f7-a8a16590cbcf
file = open(r"D:\informaticsclass\egeinfo\tests\profimatika1\26 (2).txt")
# 2035 50000
workers = sorted([(int(i.split(" ")[0]), i.split(" ")[1].strip()) for i in file], key=lambda x: [x[0], -ord(x[1])])
otpechatok = workers.copy()
n = 50_000
cnt = 0
last = -1
accepted = []
while n > workers[0][0]:
    last = workers.pop(0)
    n -= last[0]
    if last[1] == "G":
        cnt += 1
    accepted.append(last)
for delta in range(10):
    for idx, jobless in enumerate(workers):
        if jobless[1] != "G": continue
        if n < delta: break
        for i, curr in enumerate(accepted):
            if jobless[0] - delta == curr[0]:
                n -= delta
                cnt += 1
                accepted[i] = jobless
                del workers[idx]
    print(cnt, n)


# potential = []
# for i in range(len(accepted)):
#     if accepted[i][1] == "D":
#         for idx, worker in enumerate(otpechatok):
#             if worker[1] == "G" and worker[0] > accepted[i][0]:
#                 potential.append((accepted[i][0], worker[0]))
#                 del otpechatok[idx]
#                 break
    
# potential = sorted(potential, key=lambda x: abs(x[0] - x[1]))
# print(cnt, n)
# print(potential)
# for i in potential:
#     delta = abs(i[0] - i[1])
#     print(n, cnt)
#     if n - delta >= 0:
#         n -= delta
#         cnt += 1
#     print(n, cnt)
# print(cnt, n)