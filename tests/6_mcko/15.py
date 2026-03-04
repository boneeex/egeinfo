for A in range(39721, 39721 + 1):
    flag = True
    for x in range(1, 40000):
        for y in range(1, 40000):
            if not ((39_762 != y + 6 * x) or (A > x) and (A > y)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
print(A)