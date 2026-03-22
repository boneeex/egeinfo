from string import printable
alp = printable[:27]

def trans(n, base):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s += alp[n % base]
        n //= base
    return s[::-1]

print(len(trans(24 ** 655 - 8 ** 656, 27)))
print(len(trans(10 ** 4350, 27)))   
import math
x = 27 ** 3039 - 24 ** 655 + 8 ** 656
print(math.ceil(math.log10(x)))