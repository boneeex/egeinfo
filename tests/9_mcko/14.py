from string import printable
alp = printable[:49]

def trans(n, base):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s += printable[n % base]
        n //= base
    return s[::-1]

exp = 5 * 2401 ** 160 + 4 * 343 ** 165 - 3 * 49 ** 170 + 2 * 7 ** 175 - 2400
exp = trans(exp, 49)
n1 = [i for i in exp if printable.index(i) <= 9]
print(len(n1))