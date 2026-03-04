def pr_m(x, p = 2):
    for d in range(p, int(x ** 0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x // d, d)
    return [x]

n = 18_974_447
res = []
while len(res) < 5:
    n += 1
    pr = pr_m(n)
    if len(pr) != 2:
        continue
    flag = True
    for y in pr:
        n1 = [1 for i in range(1, len(str(y))) if str(y)[i] + str(y)[i - 1] in ["34", "43"]]
        if len(n1) != 1:
            flag = False
            break
    if flag:
        res.append((n, min(pr)))
for i in res:
    print(i)