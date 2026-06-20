def find_denom(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return set(res)
    if not res: return 0
    return int(sum(set(res)) / len(set(res)))

n = 750_000
res = []
while len(res) != 5:
    n += 1
    f = find_denom(n)
    if f % 7 == 6:
        res.append((n, f))
[print(*i) for i in res]