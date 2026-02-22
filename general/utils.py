file = open(r"D:\Study\egeinfo\24\24_18530.txt").readline()
dc = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": []}

for lit in dc.keys():
    l = lit.capitalize()
    dc[lit] = list(map(len, file.split(l)))

def find_max_sequence(spl: list) -> int:
    mx = 0
    cnt = 0
    d = -1
    for i in range(1, len(spl)):
        a = spl[i - 1]
        b = spl[i - 0]
        if a != b:
            mx = max(mx, cnt * d + cnt + 1)
            cnt = 0
            d = b
        else:
            cnt += 1
    return mx
mx = 0
for key, value in dc:
    mx = max(mx, find_max_sequence(value))
print(mx)