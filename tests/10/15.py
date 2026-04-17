for A in range(10 ** 3, 1, -1):
    if all((x * y > A) or (x > y) or (11 > x) for x in range(10 ** 3) for y in range(10 ** 3)):
        print(A)
        break
