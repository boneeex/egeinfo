p = range(5, 280 + 1)
q = range(295, 400 + 1)
r = range(375, 450 + 1)
# ((x∈Q)→(x∈P))∨(¬(x∈A)→(x∈R))
# not Q or P or A or R
p = set(p)
r = set(r)
print(p | r)
# ответ 375 - 295 = 80