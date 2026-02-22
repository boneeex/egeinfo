# file = open(r"D:\Study\egeinfo\24\24_18530.txt").readline()
# dc = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": []}

# for lit in dc.keys():
#     l = lit.capitalize()
#     dc[lit] = list(map(len, file.split(l)))

# def find_max_sequence(spl: list) -> int:
#     mx = 0
#     cnt = 0
#     d = -1
#     for i in range(1, len(spl)):
#         a = spl[i - 1]
#         b = spl[i - 0]
#         if a != b:
#             mx = max(mx, cnt * d + cnt + 1)
#             cnt = 0
#             d = b
#         else:
#             cnt += 1
#     return mx
# mx = 0
# for key, value in dc:
#     mx = max(mx, find_max_sequence(value))
# print(mx)

file = open(r"D:\Study\egeinfo\24\24__3091 (1).txt")

def check_palindrom(spl: list) -> bool:
    lst = list(set([i for i in spl if spl.count(i) % 2]))
    if len(lst) != 1: return False
    ancestor = spl.copy()
    # если символ, встречающийся нечетное кол-во раз, стоит посередине
    if spl[3] == lst[0]:
        for left_idx in range(3):
            for right_idx in range(4, 7):
                spl[left_idx], spl[right_idx] = spl[right_idx], spl[left_idx]
                if spl[:3] == spl[4:][::-1]: 

                    return True
                else:
                    spl = ancestor.copy()
    # если символ, встречающийся нечетное кол-во раз, не стоит посередине
    # то пытаемся его с кем то поменять
    for i in range(len(spl)):
        spl[i], spl[3] = spl[3], spl[i]
        if spl[:3] == spl[4:][::-1]: 
            return True
        else:
            spl = ancestor.copy()
    return False

cnt = 0
for line in file:
    for i in range(7, len(line)):
        if check_palindrom(list(line[i - 7:i])):
            cnt += 1
            break

print(cnt)