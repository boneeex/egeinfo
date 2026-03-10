for A in range(1, 10**6):
    if all((78125 != y + 4 * x) or (A > x) and (A > y) for x in range(1, 10 ** 5) for y in range(1, 10 ** 5)):
        print(A)
        break