def trans(n, base):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

for n in range(10 ** 5, 1, -1):
    nw = trans(n, 8)
    even = [int(i) for i in nw if int(i) % 2 == 0]
    odd = [int(i) for i in nw if int(i) % 2 == 1]
    if len(even) > len(odd):
        nw = nw + trans(sum(even), 8)
    if len(even) < len(odd):
        nw = nw + trans(sum(odd), 8)
    if len(even) == len(odd):
        nw = nw + trans(sum(even) // 2, 8)

    r = int(nw, 8)
    if r <= 870:
        print(n)
        break