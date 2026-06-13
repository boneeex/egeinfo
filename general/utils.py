# # # # file = open(r"D:\Study\egeinfo\24\24_18530.txt").readline()
# # # # dc = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": []}

# # # # for lit in dc.keys():
# # # #     l = lit.capitalize()
# # # #     dc[lit] = list(map(len, file.split(l)))

# # # # def find_max_sequence(spl: list) -> int:
# # # #     mx = 0
# # # #     cnt = 0
# # # #     d = -1
# # # #     for i in range(1, len(spl)):
# # # #         a = spl[i - 1]
# # # #         b = spl[i - 0]
# # # #         elif a != b:
# # # #             mx = max(mx, cnt * d + cnt + 1)
# # # #             cnt = 0
# # # #             d = b
# # # #         else:
# # # #             cnt += 1
# # # #     return mx
# # # # mx = 0
# # # # for key, value in dc:
# # # #     mx = max(mx, find_max_sequence(value))
# # # # print(mx)

# # # # file = open(r"D:\Study\egeinfo\24\24__3091 (1).txt")

# # # # def check_palindrom(spl: list) -> bool:
# # # #     lst = list(set([i for i in spl elif spl.count(i) % 2]))
# # # #     elif len(lst) != 1: return False
# # # #     ancestor = spl.copy()
# # # #     # если символ, встречающийся нечетное кол-во раз, стоит посередине
# # # #     elif spl[3] == lst[0]:
# # # #         for left_idx in range(3):
# # # #             for right_idx in range(4, 7):
# # # #                 spl[left_idx], spl[right_idx] = spl[right_idx], spl[left_idx]
# # # #                 elif spl[:3] == spl[4:][::-1]: 

# # # #                     return True
# # # #                 else:
# # # #                     spl = ancestor.copy()
# # # #     # если символ, встречающийся нечетное кол-во раз, не стоит посередине
# # # #     # то пытаемся его с кем то поменять
# # # #     for i in range(len(spl)):
# # # #         spl[i], spl[3] = spl[3], spl[i]
# # # #         elif spl[:3] == spl[4:][::-1]: 
# # # #             return True
# # # #         else:
# # # #             spl = ancestor.copy()
# # # #     return False

# # # # cnt = 0
# # # # for line in file:
# # # #     for i in range(7, len(line)):
# # # #         elif check_palindrom(list(line[i - 7:i])):
# # # #             cnt += 1
# # # #             break

# # # # print(cnt)

# # # # file = open(r"D:\Study\egeinfo\24\24_18284.txt").readline().strip()

# # # # l = o = v = e = []
# # # # mn = 10 ** 7
# # # # for i in range(len(file)):
# # # #     s = file[i]
# # # #     if s == "L":
# # # #         l.append(i)
# # # #     elif s == "O":
# # # #         o.append(i)
# # # #     elif s == "V":
# # # #         v.append(i)
# # # #     elif s == "E":
# # # #         e.append(i)

# # # # for i in range(len(l)):
# # # #     j = 0 
# # # #     while o[j] <= l[i]:
# # # #         j += 1
# # # #     k = 0
# # # #     while v[k] <= o[j]:
# # # #         k += 1
# # # #     z = 0
# # # #     while e[z] <= v[k]:
# # # #         z += 1
# # # #     mn = min(mn, e[z] - l[i] + 1)

# # # # print(mn)



# # # with open(r"D:\Study\egeinfo\24\24_18239.txt") as f:
# # #   text = f.read()

# # # while "--" in text:
# # #   text = text.replace("--", " -", 1)

# # # while "  " in text:
# # #   text = text.replace("  ", " ")

# # # text = text.split(" ")
# # # m = 0

# # # print(1)

# # # for st in text:
# # #   if len(st) > m:
# # #     st += '-'
# # #     a = [i for i in range(len(st)) if st[i] == '-']
# # #     for i in range(len(a)):
# # #       for j in range(i + 1, len(a)):
# # #         e = eval(st[a[i]:a[j]])
# # #         if e > -20_000:
# # #           m = max(m, len(st[a[i]:a[j]]))
# # #         else:
# # #           break
# # #     for i in range(len(a)):
# # #       for j in range(i + 1, len(a)):
# # #         e = eval(st[a[i] + 1:a[j]])
# # #         if e > -20_000:
# # #           m = max(m, len(st[a[i] + 1:a[j]]))
# # #         else:
# # #           break

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_8616.txt")
# # # # 10000
# # # # 100
# # # dentists = [-1 for i in range(100)]
# # # clients = [list(map(int, line.split(" "))) for line in file]
# # # success = []

# # # for client in clients:
# # #     time, id = client[0], client[1] - 1
# # #     if time > 810: continue
# # #     if dentists[id] < time:
# # #         dentists[id] = time + 30
# # #         success.append(id + 1)
# # #     else:
# # #         for i in range(len(dentists)):
# # #             if dentists[i] < time:
# # #                 dentists[i] = time + 30
# # #                 success.append(i + 1)
# # #                 break
# # # print(len(success), success[-1])

# # # def pr_m(x, p=2):
# # #     for d in range(p, int(x ** 0.5) + 1):
# # #         if x % d == 0:
# # #             return [d] + pr_m(x // d, d)
# # #     return [x]

# # # from itertools import *
# # # from math import prod
# # # def get_deviders(pr: list) -> list:
# # #     new_pr = []
# # #     for i in range(1, len(pr) + 1):
# # #         for var in permutations(pr, i):
# # #             new_pr.append(prod(list(var)))
# # #     return set(new_pr)

# # # print(sorted(get_deviders(pr_m(24))))

# # # file = open(r"D:\informaticsclass\egeinfo\24\24_9552.txt").readline()

# # # lst = [0 for i in range(len(file))]
# # # for i in range(len(file)):
# # #     try:
# # #         pc = file[i - 1:i + 1]
# # #         csgo = file[i - 3:i + 1]
# # #         if pc == "PC":
# # #             lst[i] = 2 + lst[i - 2]
# # #         if csgo == "CSGO":
# # #             lst[i] = 4 + lst[i - 4]
# # #     except:
# # #         continue

# # # print(max(lst))
# # # print(lst[:1000])

# # # file = open(r"D:\informaticsclass\egeinfo\24\24_9552.txt").readline()
# # # from re import *

# # # pattern = "((CSGO)|(PC))+"
# # # pattern = f"(?=({pattern}))"

# # # mx = 0
# # # iss = []
# # # for i in finditer(pattern, file):
# # #     mx = max(mx, len(i.group(1)))
# # #     iss.append(i.group(1))
# # # print(mx)
# # # print(max(iss, key=len))

# # # from itertools import product

# # # alp = range(0, 10)

# # # for guys in product(alp, repeat=7):
# # #     for girls in product(alp, repeat=7):
# # #         n1 = [i for i in guys if guys.count(i) != 1]
# # #         n2 = [i for i in girls if girls.count(i) != 1]
# # #         if min(girls) < max(guys):
# # #             print(*guys)
# # #             print(*girls)
# # #             break

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_8581.txt")
# # # # 5000 – количество упаковок привезенной продукции
# # # # 500 – количество холодильных камер
# # # # 6000 - вместимость каждой из холодильных камер в кг
# # # storage = [6000] * 500
# # # packages = sorted([int(line) for line in file], reverse=True)

# # # last = 0
# # # left = 0
# # # for idx, weight in enumerate(storage):
# # #     curr_weight = weight
# # #     while packages and curr_weight >= packages[0]:
# # #         curr_weight -= packages[0]
# # #         packages.pop(0)
# # #     while packages and curr_weight >= packages[-1]:
# # #         curr_weight -= packages[-1]
# # #         packages.pop(-1) 
# # #     if not packages:
# # #         last = idx + 1
# # #         left = curr_weight
# # #         break
# # # print(last, left)

# # # from math import *
# # # file = open(r"D:\informaticsclass\egeinfo\26\26_19599.txt")
# # # # 5555
# # # gladiators = sorted([list(map(int, line.split(" "))) for line in file], key=lambda x: x[0])
# # # for i in range(len(gladiators)):
# # #     if gladiators[i][1] == -1:
# # #         continue
# # #     if gladiators[gladiators[i][2] - 1][1] != -1:
# # #         gladiators[gladiators[i][2] - 1][1] += gladiators[i][1]
    
# # #     for y in range(3, 6):
# # #         if gladiators[gladiators[i][y] - 1][1] == -1:
# # #             continue
# # #         if gladiators[i][1] > gladiators[gladiators[i][y] - 1][1]:
# # #             gladiators[i][1] = ceil(gladiators[i][1] * 2 / 3)
# # #             gladiators[gladiators[i][y] - 1][1] = -1
# # #         elif gladiators[i][1] < gladiators[gladiators[i][y] - 1][1]:
# # #             gladiators[i][1] = -1
# # #             gladiators[gladiators[i][y] - 1][1] = ceil(gladiators[gladiators[i][y] - 1][1] * 2 / 3)
# # #             break
# # #         elif gladiators[i][1] == gladiators[gladiators[i][y] - 1][1]:
# # #             gladiators[i][1] = -1
# # #             gladiators[gladiators[i][y] - 1][1] = -1
# # #             break

# # # res = [i[1] for i in gladiators if i[1] != -1]
# # # print(len(gladiators) - len(res), max(res))

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_8432.txt")
# # # # 888
# # # light_park = [[0 for i in range(1440)] for i in range(70)]
# # # heavy_park = [[0 for i in range(1440)] for i in range(30)]
# # # cars = sorted([[int(line.split(" ")[0]), int(line.split(" ")[1]), line.split(" ")[2].strip()] for line in file])

# # # micro = 0
# # # rejected = 0
# # # for idx, car in enumerate(cars):
# # #     start, duration, typec = car
# # #     flag = False
# # #     if typec == "A":
# # #         for i in range(len(light_park)):
# # #             if not sum(light_park[i][start:start + duration]):
# # #                 light_park[i][start:start + duration] = [1] * duration
# # #                 flag = True
# # #                 break
# # #         if not flag:
# # #             for i in range(len(heavy_park)):
# # #                 if not sum(heavy_park[i][start:start + duration]):
# # #                     heavy_park[i][start:start + duration] = [1] * duration
# # #                     flag = True
# # #                     break
# # #     if typec == "B":
# # #         for i in range(len(heavy_park)):
# # #             if not sum(heavy_park[i][start:start + duration]):
# # #                 heavy_park[i][start:start + duration] = [1] * duration
# # #                 flag = True
# # #                 micro += 1
# # #                 break
# # #     if flag == False:
# # #         rejected += 1

# # # print(micro, rejected)

# # # file = open(r"D:\Study\egeinfo\26\26_17643.txt")
# # # n = int(file.readline())
# # # lines = [list(map(int, line.split(" "))) for line in file]
# # # sr = sum([i[1] for i in lines]) / len(lines)
# # # dc = {}
# # # # key = art
# # # # value = [sum_price, released, instorage, poor_or_rich]

# # # for line in lines:
# # #     art, price, status = line
# # #     if price > sr:
# # #         if status == 1:
# # #             try:
# # #                 dc[art][0] += 0
# # #                 dc[art][1] += 1
# # #             except:
# # #                 dc[art] = [price, 1, 0, True]
# # #         else:
# # #             try:
# # #                 dc[art][0] += price
# # #                 dc[art][2] += 1
# # #             except:
# # #                 dc[art] = [price, 0, 1, True]
# # #     else:
# # #         if status == 1:
# # #             try:
# # #                 dc[art][0] += 0
# # #                 dc[art][1] += 1
# # #             except:
# # #                 dc[art] = [price, 1, 0, False]
# # #         else:
# # #             try:
# # #                 dc[art][0] += price
# # #                 dc[art][2] += 1
# # #             except:
# # #                 dc[art] = [price, 0, 1, False]

# # # dc = sorted(dc.items(), key=lambda x: [x[1], x[-1]])[::-1][:10]
# # # print(dc)

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_2653.txt")
# # # n = int(file.readline())
# # # file = sorted([int(line) for line in file])
# # # dp = [0 for i in range(sum(file) + 1)]
# # # dp[0] = 1

# # # sm = 0
# # # for idx in file:
# # #     new_dp = dp.copy()
# # #     for i in range(sm + 1):
# # #         if dp[i] == 1:
# # #             new_dp[i + idx] = 1
# # #     dp = new_dp.copy()
# # #     dp[idx] = 1
# # #     sm += idx
# # # print(dp.count(0), len(dp) - dp[::-1].index(0) - 1)

# # # file = open(r"D:\informaticsclass\egeinfo\24\24_22446.txt").readline()
# # # file = file.replace("LND", "*")
# # # file = file.split("*")
# # # mx = 0
# # # for i in range(len(file) - 10_000):
# # #     first = file[i] + "LND"
# # #     last = "LND" + file[i + 10_000]
# # #     mx = max(mx,
# # #              len(first) - first.find("L") + 9999 * 3 + last.rfind("L") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
# # #     mx = max(mx,
# # #              len(first) - first.find("N") + 9999 * 3 + last.rfind("N") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
# # #     mx = max(mx,
# # #              len(first) - first.find("D") + 9999 * 3 + last.rfind("D") + sum(len(file[y]) for y in range(i + 1, i + 10_000)))
# # # print(mx)

# # # file = open(r"D:\informaticsclass\egeinfo\26\26 (2).txt")

# # # n, k = map(int, file.readline().split())
# # # workers = [[0] * 28800 for i in range(n)]
# # # captchas = sorted([int(line) for line in file])

# # # success = 0
# # # last_worker = 0
# # # for captcha in captchas:
# # #     for idx, worker in enumerate(workers):
# # #         if worker[captcha: captcha + 60] == [0] * 60:
# # #             workers[idx][captcha: captcha + 60] = [1] * 60
# # #             success += 1
# # #             if idx == len(workers) - 1:
# # #                 last_worker += 1
# # #             break

# # # print(success, last_worker)

# # # file = open(r"D:\informaticsclass\egeinfo\24\24 (2).txt").readline()
# # # file = file.split("A")

# # # mx = 0
# # # for i in range(len(file) - 3):
# # #     window = file[i:i + 3]
# # #     if window[0] == window[1] and window[0] == window[2]:
# # #         mx = max(mx, sum(list(map(len, window))) + 4)
# # # print(mx)


# # # file = open(r"D:\informaticsclass\egeinfo\24\24_18530.txt").readline()
# # # idxs = [i for i in range(len(file)) if file[i] in ["A", "E"]]
# # # start = diff = mx = last = 0
# # # for i in range(1, len(file)):
# # #     if i - last != diff:
# # #         mx = max(mx, i - start + 1)
# # #         start = last + 1

# # # from itertools import product

# # # res = []
# # # for i in product("0123456", repeat=2):
# # #     res.append(i)
# # # res = set(res)
# # # print(len(res))
# # # print(res)

# # # file = open(r"D:\informaticsclass\egeinfo\24\24_28006.txt").readline()
# # # # file = "(((56+-+00(0678-89)(78-9)(322+7))"
# # # file = file.replace("(", "I").replace(")", "J")
# # # print(file)
# # # from re import *

# # # num1 = "(([1-9][0-9]*[02468])|([2468]))"
# # # num2 = "(([1-9][0-9]*[13579])|([13579]))"
# # # pattern = f"([I]({num1}[+-]{num2})[J])*"    
# # # pattern = f"(?=({pattern}))"
# # # mx = 0
# # # res = []
# # # for i in finditer(pattern, file):
# # #     mx = max(mx, len(i.group(1)))
# # # print(mx)

# # # mn = 10 ** 7
# # # mx = 0
# # # cnt_30 = 0
# # # n = int(input())
# # # for i in range(n):
# # #     car = int(input())
# # #     if car <= 30: cnt_30 += 1
# # #     mn = min(mn, car)
# # #     mx = max(mx, car)
# # # print(mx - mn)
# # # print(cnt_30)

# # # from itertools import *

# # # res = []
# # # for var in permutations(range(1, 40), 5):
# # #     res.append((var, sum(var)))
# # # print(sorted(res, key=lambda x: -x[-1]))
# # # l = "1234567"
# # # print(l.rfind("3"))

# # # def F(n):
# # #     res = 1
# # #     while n >= 10:
# # #         res *= (n + 3) 
# # #         n -=3
# # #     return res 

# # # print((F(247563)/519−477×F(247560))/F(247557))

# # # from string import printable
# # # alp = printable[:36]
# # # def trans(n, base):
# # #     if n == 0:
# # #         return "0"
# # #     s = ""
# # #     while n > 0:
# # #         s += alp[n % base]
# # #         n //= base
# # #     return s[::-1]
# # # # 
# # # exp = 5 * 1296**2021 - 4 * 216 ** 2022 + 3*36 ** 2023 - 2 * 6**2024 - 2025

# # # cnt = 0
# # # for i in trans(exp, 36):
# # #     if alp.index(i) % 2 == 0:
# # #         cnt += 1
# # # print(cnt)

# # # def perevod(n, system):
# # #     s=[]
# # #     while n>0:
# # #         s.append(str(n%system))
# # #         n=n//system

# # #     return s[::-1]

# # # number=5 * 1296**2021-4* 216 ** 2022+3*36 ** 2023-2*6**2024-2025
# # # number=perevod(number, 36)

# # # count =0
# # # for i in number:
# # #     if int(i) % 2==0:
# # #         count+=1

# # # print(count)

# # # from ipaddress import *

# # # net = ip_network("68.203.243.87/255.255.224.0", 0)
# # # for ip in net:
# # #     print(ip)

# # # # 68.203.255.254
# # # print(68 + 203 + 255 + 254)

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_17643.txt")

# # # n = int(file.readline())
# # # items = [list(map(int, i.split())) for i in file]
# # # sr = sum(i[1] for i in items) / len(items)
# # # expensive = [i for i in items if i[1] > sr]
# # # dc = {}

# # # for i in expensive:
# # #     art, cost, status = i
# # #     try:
# # #         dc[art].append((cost, status))
# # #     except:
# # #         dc[art] = [(cost, status)]

# # # res = []
# # # for art, content in dc.items():
# # #     res.append((
# # #                 # sold
# # #                 sum(1 for i in content if i[1] == 1),
# # #                 # remaining
# # #                 sum(1 for i in content if i[1] == 0),
# # #                 # price
# # #                 content[0][0]
# # #                 ))


# # # res = sorted(res, key=lambda x: [-x[0], -x[2], x[1]])
# # # print(res[0])


# # # def f(n):
# # #     if n <= 1:
# # #         return n
# # #     elif n > 1 and n % 3 == 0:
# # #         return n + f(n // 3)
    
# # # for i in range(1, 10**4, 3):
# # #     if f(3 ** i) > 100: 
# # #         print(3 ** i)
# # #         break

# # # exp = 9 * 11 ** 210 + 8 * 11 ** 150 

# # # def trans(n, base):
# # #     cnt_0 = 0
# # #     if n == 0:
# # #         return "0"
# # #     s = ""
# # #     while n > 0:
# # #         if n % base == 0:
# # #             cnt_0 += 1
# # #         n //= base
# # #         if cnt_0 > 60:
# # #             return False
# # #     return cnt_0 == 60

# # # for x in range(3000, -1, -1):
# # #     if trans(exp - x, 11):
# # #         print(x)
# # #         break

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_29234.txt")
# # # k = int(file.readline())
# # # n = int(file.readline())
# # # appointments = sorted([[idx + 1] + list(map(int, line.split(" "))) for idx, line in enumerate(file.readlines())])
# # # computers = [[0] * 1440 for i in range(k)]
# # # profit_comp = {i: 0 for i in range(len(computers))}
# # # accepted = 0

# # # for appointment in appointments:
# # #     i, start, stop = appointment
# # #     time = stop - start
# # #     for idx, computer in enumerate(computers):
# # #         if computer[start:stop] == [0] * time:
# # #             computers[idx][start:stop] = [0] * time
# # #             profit_comp[idx] += time * (time + 1) // 2
# # #             accepted += 1
# # #             break
# # # print(accepted, profit_comp.items())

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_22605 (1).txt")
# # # n = int(file.readline())

# # # def find_gap(lst):
# # #     mn = 10 ** 7
# # #     for i in range(1, len(lst)):
# # #         mn = min(mn, lst[i] - lst[i - 1])
# # #         return mn
    
# # # matrix = [[] * 10_000 for i in range(10_000)]
# # # print(matrix)
# # # fired = []
# # # for i in file:
# # #     x, y, t = map(int, i.split())
# # #     try:
# # #         matrix[x - 1][y - 1].append(t)
# # #     except:
# # #         print(x - 1, y - 1)
# # #         exit()
# # #     fired.append((x - 1, y - 1))

# # # res = []
# # # for cell in fired:
# # #     x, y = cell
# # #     a = find_gap(matrix[x][y])
# # #     if a: res.append((a, x + y + 2))
# # # print(min(res))

# # # from re import *
# # # file = open(r'D:\informaticsclass\egeinfo\24\24 (9).txt').readline()
# # # pattern = "([1-9A-E])([0-9A-E])*([124578ABDE])"

# # # res = []
# # # for i in finditer(pattern, file):
# # #     i = i.group(0)
# # #     res.append((len(i), file.index(i)))
# # # print(sorted(res, reverse=True)[:3])

# # # file = open(r"D:\informaticsclass\egeinfo\26\26_9711.txt")
# # # m, n = map(int, file.readline().split())
# # # appointments = [list(map(int, line.split())) for line in file]
# # # parking_lots = [0] * (m + 1)
# # # ticks = [0] * 1440

# # # res = []
# # # for tick in range(1440):
# # #     ghost = [0] * len(parking_lots)
# # #     for app in appointments:
# # #         start, duration, id_start, id_stop = app
# # #         if tick == start:
# # #             ticks[tick] += 1
# # #             parking_lots[id_start] -= 1
# # #             res.append((id_start, parking_lots[id_start] - ghost[id_start]))
# # #         elif tick == start + duration:
# # #             parking_lots[id_stop] += 1
# # #             ghost[id_stop] += 1
# # #         else:
# # #             continue

# # # print(ticks.index(max(ticks)), min(res, key=lambda x: x[-1])[0])
# # # print(ticks[176], ticks[400])

# # file = open(r"D:\informaticsclass\egeinfo\26\26_9711.txt")
# # m, n = map(int, file.readline().split())
# # events = []
# # for _ in range(n):
# #     t, d, s, f = map(int, file.readline().split())
# #     events.append((t, -1, s))          # аренда в момент t
# #     events.append((t + d + 1, 1, f))   # возврат с t+d+1

# # events.sort()  # по времени, при равном времени сначала возвраты? Но для корректности:
# #                # если в одну минуту и возврат, и аренда, то сначала нужно увеличить баланс,
# #                # чтобы самокат, вернувшийся в эту минуту, был доступен для аренды в эту же минуту.
# #                # Поскольку возврат имеет время t+d+1, а аренда имеет время t, коллизий нет.
# #                # Но если бы были, нужно сортировать так, чтобы +1 шли перед -1.
# #                # Здесь же времена различны, так как t+d+1 > t при d>=0.

# # balance = [0] * (m + 1)   # текущий баланс (начиная с 0)
# # min_balance = [0] * (m + 1)   # минимальный достигнутый баланс для каждой парковки
# # max_rentals = 0
# # best_time = 0
# # current_rentals = 0
# # idx = 0
# # while idx < len(events):
# #     time = events[idx][0]
# #     # обрабатываем все события этого времени
# #     rent_count = 0
# #     while idx < len(events) and events[idx][0] == time:
# #         _, delta, park = events[idx]
# #         if delta == -1:
# #             rent_count += 1
# #         balance[park] += delta
# #         if balance[park] < min_balance[park]:
# #             min_balance[park] = balance[park]
# #         idx += 1
# #     # после обработки событий времени time, rent_count - количество аренд в эту минуту
# #     if rent_count > max_rentals:
# #         max_rentals = rent_count
# #         best_time = time
# #     # если равное количество, оставляем наименьшее время (первое встреченное)
# #     # в силу сортировки, время увеличивается, так что при равенстве мы не обновляем

# # # Определяем парковку с максимальным требуемым начальным количеством
# # required = [ -min_balance[i] if min_balance[i] < 0 else 0 for i in range(1, m+1) ]
# # max_required = max(required)
# # best_park = required.index(max_required) + 1  # первый с максимальным

# # # print(best_time, best_park)

# # lst_1 = [3]
# # lst_2 = [1]

# # while sum(lst_1) <= 25:
# #     lst_1.append(1 + lst_1[-1])

# # while sum(lst_2) <= 25:
# #     lst_2.append(2 + lst_2[-1])

# # print(lst_1[:len(lst_1) - 1])
# # print(lst_2[:len(lst_2) - 1])

# # for a in range(31, 40):
# #     for b in range(41, 50):
# #         if b % (b - a) == 0:
# #             print((a, b), b // (b - a), a * (b // (b - a)))

# # print(sum(list(range(10, 79))) + 94)
# # print(len(list(range(10, 80))))

# # spl = list("*" + "a" * 100 + "b" * 100 + "a" * 100 + "c" * 100 + "*")
# # state = 0
# # idx = 0
# # while True:
# #     if state == 1 and spl[idx] == "*":
# #         break
# #     elif state == 0 and spl[idx] == "*":
# #         idx += 1
# #     elif spl[idx] == "a" and state == 0:
# #         spl[idx] = "b"
# #         idx += 1
# #     elif spl[idx] == "b" and state == 0:
# #         spl[idx] = "a"
# #         idx -= 1
# #     elif spl[idx] == "c" and state == 0:
# #         spl[idx] = "b"
# #         idx += 1
# #         state = 1
# #     elif spl[idx] == "c" and state == 1:
# #         spl[idx] = "c"
# #         idx += 1
# #         state = 1
# # print(spl.count("b"))

# # print(bin(123)[2:])

# # for i in range(3000, -1, -1):
# #     n = bin(i)[2:]
# #     if n.endswith("0000100"):
# #         print(i)
# #         break

# # print(bin(2948)[2:])
# # print(bin(1924)[2:])

# # print((3496 - 764 * 3 - 114 * 2) / 122)

# print(bin(32768)[2:])

            #    vertical[row[j - 1]].index(idx_r) == len(vertical[row[j - 1]]) - 1,
            #    vertical[row[j]].index(idx_r) == len(vertical[row[j]]) - 1]

# from turtle import *

# speed(1000)
# # tracer(0)
# m = 5000

# left(90)

# begin_fill()
# for i in range(2):
#   forward(14 * m) # fd
#   left(270) #lt
#   backward(12 * m)
#   right(90)
# end_fill()

# up()

# forward(9*m)
# right(90)
# backward(7*m)
# left(90)

# down()

# begin_fill()
# for i in range(2):
#   forward(13 * m)
#   right(90)
#   forward(6 * m)
#   right(90)
# end_fill()

# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#   for y in range(-200, 200):
#     if canvas.find_overlapping(x*m, y*m, x*m, y*m) != ():
#       cnt += 1
# print(cnt)
# done()

# from turtle import *
# m = 10
# speed(1000)
# left(90)
# begin_fill()
# right(90)
# for i in range(3):
#     right(45)
#     forward(10 * m)
#     right(45)
# right(315)
# forward(10 * m)
# for i in range(2):
#     right(90)
#     forward(10 * m)
# end_fill()

# cnt = 0
# canvas = getcanvas()
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if canvas.find_overlapping(x*m, y*m, x*m, y*m) == (5,):
#             cnt += 1
# print(cnt)

# from turtle import *
# speed(1000)
# m = 30
# left(90)

# begin_fill()
# for i in range(2):
#     forward(5 * m)
#     left(90)
#     backward(13 * m)
#     left(90)
# end_fill()
# up()
# backward(10 * m)
# right(90)
# forward(9 * m)
# left(90)
# down()
# begin_fill()
# for i in range(2):
#     forward(11 * m)
#     right(90)
#     forward(7 * m)
#     right(90)
# end_fill()

# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#   for y in range(-200, 200):
#     if canvas.find_overlapping(x*m, y*m, x*m, y*m) != ():
#       cnt += 1
# print(cnt)

# from turtle import *
# left(90)
# tracer(0)
# m = 20

# right(180)
# for i in range(5):
#     forward(12 * m)
#     right(90)
#     forward(15 * m)
#     right(90)
# up()
# forward(6 * m)
# right(90)
# forward(10 * m)
# left(90)
# down()
# for i in range(7):
#     forward(10 * m)
#     right(90)
#     forward(17 * m)
#     right(90)
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x* m, y * m)
#         dot(5)
# done()

# for A in range(1000, -1, -1):
#     if all((x * y > A) or (x > y) or (11 > x) for x in range(1000) for y in range(1000)):
#         print(A)
#         break

# 
# p = {5,10,15,20,25,30}
# q = {15,18,21,24,27,30}
# print([i for i in p if i in q])

# file = open(r"D:\informaticsclass\egeinfo\24\24_23206.txt").readline()
# for i in "02468": file = file.replace(i, "*")
# file = file.split("*")[1:]

# mx = 0
# for line in file:
#     if line.count("S") < 35: continue
#     s = 0
#     for i in range(len(line)):
#         if line[i] == "S":
#             s += 1
#         if s == 35:
#             mx = max(mx, i + 2)
#         elif s > 35:
#             break
# print(mx)

# file = open(r"D:\informaticsclass\egeinfo\26\26_30401.txt")
# k, n = list(map(int, file.readline().split()))
# # id type volume timelaps
# cameras = sorted([[i+1] + list(map(int, file.readline().split())) + [[0] * 1440] for i in range(k)], key=lambda x: x[-2])
# # start stop volume type_needed 
# requests = sorted([list(map(int, file.readline().split())) for i in range(n)], key=lambda x: [x[0], x[1]])
# print(cameras[:4])

# res1 = 0
# res2 = []
# for req in requests:
#     start, stop, volume, type_n = req
#     duration = stop - start
#     for idx, cam in enumerate(cameras):
#         id, type_exist, vol_exist, laps = cam
#         if type_n == type_exist and volume <= vol_exist and laps[start:stop] == [0] * duration:
#             cameras[idx][-1][start:stop] = [1] * duration
#             res1 += 1
#             res2.append((start, id))
#             break

# # print(res1, sorted(res2, key=lambda x: [-x[0], x[1]]))

file = open(r"D:\informaticsclass\egeinfo\26\26_30401.txt")
k, n = list(map(int, file.readline().split()))
# id type volume timelaps
cameras = sorted([[i+1] + list(map(int, file.readline().split())) + [[0] * 1440] for i in range(k)], key=lambda x: x[-2])
# start stop volume type_needed 
requests = sorted([list(map(int, file.readline().split())) for i in range(n)], key=lambda x: [x[0], x[1]])
print(cameras)

res1 = 0
res2 = []
for req in requests:
    start, stop, volume, type_n = req
    duration = stop - start
    for idx, cam in enumerate(cameras):
        id, type_exist, vol_exist, laps = cam
        if type_n == type_exist and volume <= vol_exist and laps[start:stop] == [0] * duration:
            cameras[idx][-1][start:stop] = [1] * duration
            res1 += 1
            res2.append((start, id))
            break

print(res1, sorted(res2, key=lambda x: [-x[0], x[1]])[0][-1])