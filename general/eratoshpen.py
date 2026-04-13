# def sieve(n):
#     lst = [*range(2, n + 1)]
#     for sym in lst:
#         if sym != 0:
#             for i in range(lst.index(sym) + sym, len(lst), sym):
#                 lst[i] = 0
#         else:
#             continue
#     return [i for i in lst if i]

# print(*range(2, 30))
# print(sieve(30))

# def sieve(n):
#     lst = [*range(2, n + 1)]
#     length = len(lst)
#     for idx, sym in enumerate(lst):
#         if sym == 0:
#             continue
#         if sym * sym > n:
#             break
#         start = sym * sym - 2
#         for i in range(start, length, sym):
#             lst[i] = 0
#     return [i for i in lst if i]

# print(sieve(10 ** 7))

# работает

file = open(r"D:\Study\egeinfo\26\26_2653.txt")
n = int(file.readline())
file = sorted([int(line) for line in file])
dp = [0 for i in range(sum(file) + 1)]
for i in file:
    dp[i] = 1
print(dp)
for i in range(len(dp)):
    for y in range(i):
        dp[i + y] = 1
print(dp)