from itertools import product

alp = sorted('О, Д, С, А, Ц, Л, Ф, Щ'.split(", "))
cnt = 0
for var in product(alp, repeat=4):
    cnt += 1
    if cnt % 2 and var[0] != "А" and var[-1] != "А" and var.count("Л") >= 3:
        print(cnt)
        print(var)
        break