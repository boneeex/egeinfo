def trans(n, base):
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

res = []
for n in range(1, 10000):
    nw = trans(n, 3)
    if n % 3 == 0:
        nw = nw + nw[len(nw) - 2:]
    else:
        nw = nw + trans(sum(list(map(int, list(nw)))) * 2, 3)
    r = int(nw, 3)
    if r > 189 and r % 2 == 0:
        res.append(r)
print(min(res))
