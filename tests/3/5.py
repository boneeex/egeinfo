def trans(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

best_res = 10 ** 5
best_r = 0

for n in range(1, 10 ** 5):
    nw = trans(n)
    if n % 3 == 0:
        nw = nw + nw[len(nw) - 2:]
    else:
        nw = nw + trans(sum(list(map(int, nw))) * 3)
    
    r = int(nw, 3)
    if abs(r - 826) < best_res:
        best_r = r

print(best_r)