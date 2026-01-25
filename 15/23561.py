def dl(x, y):
    if x % y == 0: return True
    return False

mx = 0
for A in range(1, 10*5):
    flag = True
    for x in range(50, 1000):
        if not(dl(x, 128) <= (not dl(x, A) <= (not dl(x, 80)))):
            flag = False
            break
    if flag:
        mx = A

print(mx)

# тут почему то выводит 0 я хз
# ДЕЛ(х,128)→(¬ДЕЛ(х,А)→¬ДЕЛ(х,80))
# ДЕЛ(х,128)→(ДЕЛ(х,А) или ¬ДЕЛ(х,80))
# не ДЕЛ(х,128) или ДЕЛ(х,А) или не ДЕЛ(х,80)
# значит рассмотрим случай когда x делится и на 80 и на 128 это НОК(128, 80) = 640

def evk(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(128 * 80 / evk(128, 80))