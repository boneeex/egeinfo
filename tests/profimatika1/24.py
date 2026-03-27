file = open(r"D:\Study\egeinfo\tests\profimatika1\24.txt").readline()
from re import *

pattern = "[a-z]+[@][a-z]+[_][a-z]+"
pattern = f"(?=({pattern}))"

res = []
for i in finditer(pattern, file):
    res.append(i.group(1))
res = max(res, key=len)
print(len(res) - res.find("@") - 1)