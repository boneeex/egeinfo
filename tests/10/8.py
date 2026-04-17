from itertools import product

alp = "ТЕОРИЯ"
alp = sorted(alp)

lst = [i for i in product(alp, repeat=6)][::-1]
cnt = len(lst)
for i in lst:
    if cnt % 2 == 1 and i[0] not in "РТЯ" and i.count("И") >= 2:
        print(cnt)
        print(i)
        break
    cnt -= 1
