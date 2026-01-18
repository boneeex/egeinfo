def trans(n):
    s = ""
    while n > 0:
        s += str(n % 8)
        n //= 8
    return s[::-1]

mn = 10 ** 7

for n in range(483, 10 ** 6):
    new_n = trans(n)
    sm = trans(sum(list(map(int, new_n))))
    if int(sm) % 2 == 0:
        new_n = new_n + sm
    else:
        new_n = sm + new_n
    r = int(new_n, 8)
    mn = min(r, mn)

print(mn)