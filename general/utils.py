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

def pr_m(x, p = 2):
    for d in range(p, int(x ** 0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x // d, d)
    return [x]

