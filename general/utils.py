# # file = open(r"D:\Study\egeinfo\24\24_18530.txt").readline()
# # dc = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": []}

# # for lit in dc.keys():
# #     l = lit.capitalize()
# #     dc[lit] = list(map(len, file.split(l)))

# # def find_max_sequence(spl: list) -> int:
# #     mx = 0
# #     cnt = 0
# #     d = -1
# #     for i in range(1, len(spl)):
# #         a = spl[i - 1]
# #         b = spl[i - 0]
# #         elif a != b:
# #             mx = max(mx, cnt * d + cnt + 1)
# #             cnt = 0
# #             d = b
# #         else:
# #             cnt += 1
# #     return mx
# # mx = 0
# # for key, value in dc:
# #     mx = max(mx, find_max_sequence(value))
# # print(mx)

# # file = open(r"D:\Study\egeinfo\24\24__3091 (1).txt")

# # def check_palindrom(spl: list) -> bool:
# #     lst = list(set([i for i in spl elif spl.count(i) % 2]))
# #     elif len(lst) != 1: return False
# #     ancestor = spl.copy()
# #     # если символ, встречающийся нечетное кол-во раз, стоит посередине
# #     elif spl[3] == lst[0]:
# #         for left_idx in range(3):
# #             for right_idx in range(4, 7):
# #                 spl[left_idx], spl[right_idx] = spl[right_idx], spl[left_idx]
# #                 elif spl[:3] == spl[4:][::-1]: 

# #                     return True
# #                 else:
# #                     spl = ancestor.copy()
# #     # если символ, встречающийся нечетное кол-во раз, не стоит посередине
# #     # то пытаемся его с кем то поменять
# #     for i in range(len(spl)):
# #         spl[i], spl[3] = spl[3], spl[i]
# #         elif spl[:3] == spl[4:][::-1]: 
# #             return True
# #         else:
# #             spl = ancestor.copy()
# #     return False

# # cnt = 0
# # for line in file:
# #     for i in range(7, len(line)):
# #         elif check_palindrom(list(line[i - 7:i])):
# #             cnt += 1
# #             break

# # print(cnt)

# # file = open(r"D:\Study\egeinfo\24\24_18284.txt").readline().strip()

# # l = o = v = e = []
# # mn = 10 ** 7
# # for i in range(len(file)):
# #     s = file[i]
# #     if s == "L":
# #         l.append(i)
# #     elif s == "O":
# #         o.append(i)
# #     elif s == "V":
# #         v.append(i)
# #     elif s == "E":
# #         e.append(i)

# # for i in range(len(l)):
# #     j = 0 
# #     while o[j] <= l[i]:
# #         j += 1
# #     k = 0
# #     while v[k] <= o[j]:
# #         k += 1
# #     z = 0
# #     while e[z] <= v[k]:
# #         z += 1
# #     mn = min(mn, e[z] - l[i] + 1)

# # print(mn)



# with open(r"D:\Study\egeinfo\24\24_18239.txt") as f:
#   text = f.read()

# while "--" in text:
#   text = text.replace("--", " -", 1)

# while "  " in text:
#   text = text.replace("  ", " ")

# text = text.split(" ")
# m = 0

# print(1)

# for st in text:
#   if len(st) > m:
#     st += '-'
#     a = [i for i in range(len(st)) if st[i] == '-']
#     for i in range(len(a)):
#       for j in range(i + 1, len(a)):
#         e = eval(st[a[i]:a[j]])
#         if e > -20_000:
#           m = max(m, len(st[a[i]:a[j]]))
#         else:
#           break
#     for i in range(len(a)):
#       for j in range(i + 1, len(a)):
#         e = eval(st[a[i] + 1:a[j]])
#         if e > -20_000:
#           m = max(m, len(st[a[i] + 1:a[j]]))
#         else:
#           break

# file = open(r"D:\informaticsclass\egeinfo\26\26_8616.txt")
# # 10000
# # 100
# dentists = [-1 for i in range(100)]
# clients = [list(map(int, line.split(" "))) for line in file]
# success = []

# for client in clients:
#     time, id = client[0], client[1] - 1
#     if time > 810: continue
#     if dentists[id] < time:
#         dentists[id] = time + 30
#         success.append(id + 1)
#     else:
#         for i in range(len(dentists)):
#             if dentists[i] < time:
#                 dentists[i] = time + 30
#                 success.append(i + 1)
#                 break
# print(len(success), success[-1])

# def pr_m(x, p=2):
#     for d in range(p, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return [d] + pr_m(x // d, d)
#     return [x]

# from itertools import *
# from math import prod
# def get_deviders(pr: list) -> list:
#     new_pr = []
#     for i in range(1, len(pr) + 1):
#         for var in permutations(pr, i):
#             new_pr.append(prod(list(var)))
#     return set(new_pr)

# print(sorted(get_deviders(pr_m(24))))

# file = open(r"D:\informaticsclass\egeinfo\24\24_9552.txt").readline()

# lst = [0 for i in range(len(file))]
# for i in range(len(file)):
#     try:
#         pc = file[i - 1:i + 1]
#         csgo = file[i - 3:i + 1]
#         if pc == "PC":
#             lst[i] = 2 + lst[i - 2]
#         if csgo == "CSGO":
#             lst[i] = 4 + lst[i - 4]
#     except:
#         continue

# print(max(lst))
# print(lst[:1000])

# file = open(r"D:\informaticsclass\egeinfo\24\24_9552.txt").readline()
# from re import *

# pattern = "((CSGO)|(PC))+"
# pattern = f"(?=({pattern}))"

# mx = 0
# iss = []
# for i in finditer(pattern, file):
#     mx = max(mx, len(i.group(1)))
#     iss.append(i.group(1))
# print(mx)
# print(max(iss, key=len))

# from itertools import product

# alp = range(0, 10)

# for guys in product(alp, repeat=7):
#     for girls in product(alp, repeat=7):
#         n1 = [i for i in guys if guys.count(i) != 1]
#         n2 = [i for i in girls if girls.count(i) != 1]
#         if min(girls) < max(guys):
#             print(*guys)
#             print(*girls)
#             break

# file = open(r"D:\informaticsclass\egeinfo\26\26_8581.txt")
# # 5000 – количество упаковок привезенной продукции
# # 500 – количество холодильных камер
# # 6000 - вместимость каждой из холодильных камер в кг
# storage = [6000] * 500
# packages = sorted([int(line) for line in file], reverse=True)

# last = 0
# left = 0
# for idx, weight in enumerate(storage):
#     curr_weight = weight
#     while packages and curr_weight >= packages[0]:
#         curr_weight -= packages[0]
#         packages.pop(0)
#     while packages and curr_weight >= packages[-1]:
#         curr_weight -= packages[-1]
#         packages.pop(-1) 
#     if not packages:
#         last = idx + 1
#         left = curr_weight
#         break
# print(last, left)

# from math import *
# file = open(r"D:\informaticsclass\egeinfo\26\26_19599.txt")
# # 5555
# gladiators = sorted([list(map(int, line.split(" "))) for line in file], key=lambda x: x[0])
# for i in range(len(gladiators)):
#     if gladiators[i][1] == -1:
#         continue
#     if gladiators[gladiators[i][2] - 1][1] != -1:
#         gladiators[gladiators[i][2] - 1][1] += gladiators[i][1]
    
#     for y in range(3, 6):
#         if gladiators[gladiators[i][y] - 1][1] == -1:
#             continue
#         if gladiators[i][1] > gladiators[gladiators[i][y] - 1][1]:
#             gladiators[i][1] = ceil(gladiators[i][1] * 2 / 3)
#             gladiators[gladiators[i][y] - 1][1] = -1
#         elif gladiators[i][1] < gladiators[gladiators[i][y] - 1][1]:
#             gladiators[i][1] = -1
#             gladiators[gladiators[i][y] - 1][1] = ceil(gladiators[gladiators[i][y] - 1][1] * 2 / 3)
#             break
#         elif gladiators[i][1] == gladiators[gladiators[i][y] - 1][1]:
#             gladiators[i][1] = -1
#             gladiators[gladiators[i][y] - 1][1] = -1
#             break

# res = [i[1] for i in gladiators if i[1] != -1]
# print(len(gladiators) - len(res), max(res))

# file = open(r"D:\informaticsclass\egeinfo\26\26_8432.txt")
# # 888
# light_park = [[0 for i in range(1440)] for i in range(70)]
# heavy_park = [[0 for i in range(1440)] for i in range(30)]
# cars = sorted([[int(line.split(" ")[0]), int(line.split(" ")[1]), line.split(" ")[2].strip()] for line in file])

# micro = 0
# rejected = 0
# for idx, car in enumerate(cars):
#     start, duration, typec = car
#     flag = False
#     if typec == "A":
#         for i in range(len(light_park)):
#             if not sum(light_park[i][start:start + duration]):
#                 light_park[i][start:start + duration] = [1] * duration
#                 flag = True
#                 break
#         if not flag:
#             for i in range(len(heavy_park)):
#                 if not sum(heavy_park[i][start:start + duration]):
#                     heavy_park[i][start:start + duration] = [1] * duration
#                     flag = True
#                     break
#     if typec == "B":
#         for i in range(len(heavy_park)):
#             if not sum(heavy_park[i][start:start + duration]):
#                 heavy_park[i][start:start + duration] = [1] * duration
#                 flag = True
#                 micro += 1
#                 break
#     if flag == False:
#         rejected += 1

# print(micro, rejected)

# file = open(r"D:\Study\egeinfo\26\26_17643.txt")
# n = int(file.readline())
# lines = [list(map(int, line.split(" "))) for line in file]
# sr = sum([i[1] for i in lines]) / len(lines)
# dc = {}
# # key = art
# # value = [sum_price, released, instorage, poor_or_rich]

# for line in lines:
#     art, price, status = line
#     if price > sr:
#         if status == 1:
#             try:
#                 dc[art][0] += 0
#                 dc[art][1] += 1
#             except:
#                 dc[art] = [price, 1, 0, True]
#         else:
#             try:
#                 dc[art][0] += price
#                 dc[art][2] += 1
#             except:
#                 dc[art] = [price, 0, 1, True]
#     else:
#         if status == 1:
#             try:
#                 dc[art][0] += 0
#                 dc[art][1] += 1
#             except:
#                 dc[art] = [price, 1, 0, False]
#         else:
#             try:
#                 dc[art][0] += price
#                 dc[art][2] += 1
#             except:
#                 dc[art] = [price, 0, 1, False]

# dc = sorted(dc.items(), key=lambda x: [x[1], x[-1]])[::-1][:10]
# print(dc)

# file = open(r"D:\informaticsclass\egeinfo\26\26_2653.txt")
# n = int(file.readline())
# file = sorted([int(line) for line in file])
# dp = [0 for i in range(sum(file) + 1)]
# dp[0] = 1

# sm = 0
# for idx in file:
#     new_dp = dp.copy()
#     for i in range(sm + 1):
#         if dp[i] == 1:
#             new_dp[i + idx] = 1
#     dp = new_dp.copy()
#     dp[idx] = 1
#     sm += idx
# print(dp.count(0), len(dp) - dp[::-1].index(0) - 1)

# file = open(r"D:\informaticsclass\egeinfo\24\24_22446.txt").readline()
# file = file.replace("LND", "*")
# file = file.split("*")
# mx = 0
# for i in range(len(file) - 10_000):
#     first = file[i] + "LND"
#     last = "LND" + file[i + 10_000]
#     mx = max(mx,
#              len(first) - first.find("L") + 9999 * 3 + last.rfind("L") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
#     mx = max(mx,
#              len(first) - first.find("N") + 9999 * 3 + last.rfind("N") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
#     mx = max(mx,
#              len(first) - first.find("D") + 9999 * 3 + last.rfind("D") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
# print(mx)

# file = open(r"D:\informaticsclass\egeinfo\26\26 (2).txt")

# n, k = map(int, file.readline().split())
# workers = [[0] * 28800 for i in range(n)]
# captchas = sorted([int(line) for line in file])

# success = 0
# last_worker = 0
# for captcha in captchas:
#     for idx, worker in enumerate(workers):
#         if worker[captcha: captcha + 60] == [0] * 60:
#             workers[idx][captcha: captcha + 60] = [1] * 60
#             success += 1
#             if idx == len(workers) - 1:
#                 last_worker += 1
#             break

# print(success, last_worker)

# file = open(r"D:\informaticsclass\egeinfo\24\24 (2).txt").readline()
# file = file.split("A")

# mx = 0
# for i in range(len(file) - 3):
#     window = file[i:i + 3]
#     if window[0] == window[1] and window[0] == window[2]:
#         mx = max(mx, sum(list(map(len, window))) + 4)
# print(mx)


# file = open(r"D:\informaticsclass\egeinfo\24\24_18530.txt").readline()
# idxs = [i for i in range(len(file)) if file[i] in ["A", "E"]]
# start = diff = mx = last = 0
# for i in range(1, len(file)):
#     if i - last != diff:
#         mx = max(mx, i - start + 1)
#         start = last + 1

# from itertools import product

# res = []
# for i in product("0123456", repeat=2):
#     res.append(i)
# res = set(res)
# print(len(res))
# print(res)

file = open(r"D:\informaticsclass\egeinfo\24\24_28006.txt").readline()
# file = "(((56+-+00(0678-89)(78-9)(322+7))"
file = file.replace("(", "I").replace(")", "J")
print(file)
from re import *

num1 = "(([1-9][0-9]*[02468])|([2468]))"
num2 = "(([1-9][0-9]*[13579])|([13579]))"
pattern = f"([I]({num1}[+-]{num2})[J])*"    
pattern = f"(?=({pattern}))"
mx = 0
res = []
for i in finditer(pattern, file):
    mx = max(mx, len(i.group(1)))
print(mx)