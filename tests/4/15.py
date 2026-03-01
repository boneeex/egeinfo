for A in range(10 ** 5):
    flag = True
    for x in range(10000):
        for y in range(10000):
            if not((x >= 12) or (3 * x < y) or (x * y < A)):
                flag = False 
                break
        if not flag:
            break
    if flag:
        print(A)
        break