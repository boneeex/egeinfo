# ((y+x) 
# 2
#  >1048)∨((x+20<A)∧(40−y<A))

for A in range(-1000, 1000):
    if all(((x + y) ** 2 > 1048) or ((x + 20 < A) and (40 - y < A)) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break