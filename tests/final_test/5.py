def trans(n, base):
    if n == 0: return "0"
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

for n in range(10000):
    nw = bin(n)[2:]
    if n % 3 == 0:
        nw = nw + nw[len(nw) - 3:]
    else:
        nw = nw + bin((n % 3) * 3)[2:]
    r = int(nw, 2)
    if r >= 76:
        print(n)
        break