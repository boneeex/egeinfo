def pr_m(x, p=2):
    for d in range(p, int(x ** 0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x // d, d)
    return [x]

n = 1326234
res = []
while len(res) < 5:
    n += 1
    pr = pr_m(n)
    if len(pr) != 2 or str(pr[0]).count("7") != 1 or str(pr[1]).count("7") != 1:
        continue
    res.append((n, max(pr)))

[print(*i) for i in res]