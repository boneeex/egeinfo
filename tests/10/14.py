def trans(n, base):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

exp = 9 ** 150 + 9 ** 30
for x in range(1, 3000 + 1):
    if trans(exp - x, 9).count("0") == 122:
        print(x)
        break