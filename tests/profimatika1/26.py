# https://education.yandex.ru/ege/inf/training/26/task/1?examTaskId=a1095eef-0af6-43fa-b4fd-859c2093e179&examTaskNumber=26&taskId=4ab7b0fc-334c-490e-afdf-d01720244cd1&categoryId=bef6892c-185c-4e3f-9023-80083c0cf68d
from collections import defaultdict
file = open(r"D:\informaticsclass\egeinfo\tests\profimatika1\26.txt").readlines()
# 199154 95324
districts = [int(line) for line in file[:199154]]
snowrem = sorted([tuple(map(int, line.strip().split(" "))) for line in file[199154 + 1:]])
price = defaultdict(int=0)

for i in snowrem:
    power, sm = i
    try:
        a = price[power]
    except:
        price[power] = sm

lowestp = 99024
last = 1000
for key, value in list(price.items())[::-1]:
    if value < lowestp: last, lowestp = key, value
    if value >= lowestp: 
        price[key] = (last, lowestp)

mx = 0
total = 0
for ds in districts:
    try:
        total += price[ds]
        mx = max(mx, ds)
    except:
        total += price[ds][1]
        mx = max(mx, price[ds][0])
print(total, mx)