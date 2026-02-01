# ( ¬ДЕЛ(x, 3) ∧ x ∉ {48, 52, 56} ) → (( |x – 50| ⩽ 7) → ( x in Q )) ∨ (x & A = 0)

def dl(x, n):
    if x % n == 0: return True
    return False

m = 5
Q = range(29, 48)
for A in range(1, 10 ** m):
    flag = True
    for x in range(1, 10 ** (m - 1)):
        if not((not dl(x, 3) and x not in [48, 52, 56]) <= (((abs(x - 50) <= 7) <= (x in Q)) or (x & A == 0))):
            flag = False
            break
    if flag:
        print(A)
        break

# изичная задача