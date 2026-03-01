def f(n):
    res = 0
    while n > 1:
        res += n + 3
        n -= 2
    return n + 2 + res

cnt = 0
for n in range(1, 7000):
    if f(n) < 565:
        cnt += 1
print(cnt)