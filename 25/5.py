def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

from itertools import permutations

for num in range(1_411_111_115, 1_411_111_127 + 1):
    if not ("0" in str(num)) and any([isprime(int("".join(var))) for var in set(permutations(str(num))) if int("".join(var)) != num]):
        print(num)
