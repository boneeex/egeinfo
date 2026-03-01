from fnmatch import fnmatch

def divisors_sum(n):
    s = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

cnt = 0
for num in range(1, 10**6 + 1):
    if fnmatch(str(divisors_sum(num)), "2*45"):
        cnt += 1

print(cnt)