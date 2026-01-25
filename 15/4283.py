# ((x∈P)→(x∈A))∨((x∈/A)→(x∈/Q))
# (not P or A) or (A or not Q)
# A or not P or not Q
P = {1,3,4,9,11,13,15,17,19,21}
Q = {3,6,9,12,15,18,21,24,27,30}
from math import prod

print(prod(P | Q))

# получается нам нужно покрыть объединение не P и не Q, но ответ не правильный