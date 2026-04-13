def pr_m(x, p=2):
    for d in range(p, int(x ** 0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x // d, d) 
    return [x]

def find_comb(n):
    n = str(n)
    cnt = 0
    for i in range(1, len(n)):
        if n[i - 1] + n[i] in ["13", "31"]:
            cnt += 1
        if cnt > 1:
            return False
    if cnt == 1:
        return True
    
n = 10_019_419
res = []
while len(res) < 5:
    n += 1
    pr = pr_m(n)
    if len(pr) != 2: continue
    n1 = [find_comb(i) for i in pr]
    if not all(n1): continue
    res.append((n, min(pr)))
[print(*i) for i in res]