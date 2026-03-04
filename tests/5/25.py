from math import prod
def pr_m(x, p = 2):
    for d in range(p, int(x ** 0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x // d, d)
    return [x]

lst = []
n = 24_517_512
while len(lst) < 5:
    pr = pr_m(n)
    if len(pr) == 12:
        lst.append((n, pr[-1]))
    n += 1
print(lst)