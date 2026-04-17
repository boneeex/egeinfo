def trans(n, base):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

for n in range(10 ** 5, 1, -1):
    if n % 3 == 0:
        nw = trans(n, 2) + trans(n, 2)[len(trans(n, 2)) - 3:]
    else:
        nw = trans(n, 2) + trans((n % 3) * 3, 2)
    r = int(nw, 2)
    if r < 130:
        print(n)
        break