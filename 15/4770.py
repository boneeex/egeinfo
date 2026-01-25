# На числовой прямой даны два отрезка: P=[35,55] и Q=[45,65]. Определите наименьшую возможную длину отрезка A, при котором формулы
# (x ∈ P) → (x ∈ А)
# (x ∉ A) → (x ∉ Q)
# тождественно истинны, то есть принимают значение 1 при любом значении переменной х.

# (not P or A) and (A or Q)
# (not p and (A or Q)) or (A and (A or Q))
# (not P and A) or (not P or Q) or (A and A) or (A and Q)
# (not P and A) or (not P and Q) or (A and Q)
# 