p = range(12, 62 + 1)
q = range(52, 92 + 1)

for x in range(11, 200):
    a = range(10, x+1)
    flag = True
    if not (not((x not in a) and (x in p)) or (x in q)):
        flag = False
        break
    if flag:
        print(x)
        break