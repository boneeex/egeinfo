from fnmatch import fnmatch
from collections import defaultdict
from math import prod

def sieve(n):
    lst = [*range(2, n + 1)]
    for sym in lst:
        if sym == 0:
            continue
        for i in range(sym ** 2 - 2, len(lst), sym):
            lst[i] = 0
    return [i for i in lst if i]

def denom(n, pr):
    ans = defaultdict(int)
    den = 0
    lst_of_prost = pr
    while n != 1:
        a = lst_of_prost[den]
        if n % a == 0:
            n //= a
            ans[a] += 1
        else:
            den += 1
    return ans

pr = sieve(10**9)

n = 10 ** 9
cnt = 0
while cnt < 5:
    n += 1
    if not fnmatch(str(n), "1*2*7*04"):
        continue
    a = denom(n, pr)
    n1 = prod([i + 1 for i in list(a.values())])
    if n1 == 45:
        print(n, n // min(a.keys()))
        cnt += 1