def trans(n, base):
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

for n in range(1, 10000):
    nw = trans(n, 20)
    l = len(nw)
    if l % 2 == 0:
        nw = nw[l//2:] + nw[:l//2]
    else:
        nw = nw + nw[-1]
    