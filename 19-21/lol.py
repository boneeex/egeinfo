from fnmatch import fnmatch

def denom2(n) -> set:
    ans = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ans |= {i, n // i}
    return ans

n = int(10 ** 9 ** 0.5)
cnt = 0
while cnt < 5:
    N = n ** 2
    if not fnmatch(str(N), "1*2*7*04"):
        n += 1
        continue
    n1 = denom2(N)
    if len(n1) == 43:
        print(N)
        cnt += 1
    n += 1