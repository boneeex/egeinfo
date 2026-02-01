# ((x ∈ B) ∨ ¬ (x ∈ A)) → ¬ (x ∈ C)
# not (B or not A) or not C
# (not B and A) or not C

# b = []
# for i in range(2, 211):
#     if 211 % i == 0:
#         b.append(i)
# print(*b)

# b - пустое множество
# тогда выражение преобразуется как
# A or not C    
# либо х в [4; 82] либо х не равен делителям у
# нужно чтобы все делители числа y лежали на отрезке А

best_n = 0
best_cnt = 0

for i in range(2, 10**4):
    flag = True
    cnt = 0
    for x in range(2, i): 
        if i % x == 0:
            cnt += 1
            if x < 4 or x > 82: 
                flag = False
                break
    if flag and cnt > 0:
        if cnt > best_cnt:
            best_cnt = cnt
            best_n = i

print(best_n)