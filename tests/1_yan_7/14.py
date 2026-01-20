def trans(n, base):
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

exp = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

for base in range(100, 2, -1):
    if trans(exp, base).endswith("001"):
        print(base)
        break