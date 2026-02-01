def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a and (a > 0 and b > 0 and c > 0):
        return True
    return False

def mx(a, b):
    if a > b: return a
    if a <= b: return b

m = 4
for A in range(10 ** m, 1, -1):
    flag = True
    for x in range(1, 10 ** (m - 1)):
        # ТРЕУГ(A,7,x)→((МАКС(x+5,14)⩽27)≡¬ТРЕУГ(36,21,x))
        if not (triangle(A, 7, x) <= ((mx(x + 5, 14) <= 27) == (triangle(36, 21, x) == False))):
            flag = False
            break
    if flag:
        print(A)
        break

# необъяснимо но факт
# если начинать перебор А например с 10 ** m где m > 2 программа выводит 10 ** m
# я по фану поменял for A in range(10 ** m, 1, -1): на for A in range(150, 1, -1):
#                                                                      ^ вот здесь
#  и после этого выводится правильный ответ