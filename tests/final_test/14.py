def trans(n, base):
    if n == 0: return "0"
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s[::-1]

exp = 5 ** 1000 - 5 ** 200 + 5 ** 100 - 129
print(trans(exp, 5).count("4"))