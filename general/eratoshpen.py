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

def sieve(n):
    lst = [*range(2, n + 1)]
    length = len(lst)
    for idx, sym in enumerate(lst):
        if sym == 0:
            continue
        if sym * sym > n:
            break
        start = sym * sym - 2
        for i in range(start, length, sym):
            lst[i] = 0
    return [i for i in lst if i]

print(sieve(10 ** 7))

# работает