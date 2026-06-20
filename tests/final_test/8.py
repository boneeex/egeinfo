from itertools import product, repeat

alp = "СТРЕЛА"
cnt = 0
for var in product(sorted(alp), repeat=5):
    cnt += 1
    if cnt % 2 == 0 and var[0] not in "АСТ" and var.count("Л") == 2 and "ЛЛ" not in "".join(var):
        print(cnt)