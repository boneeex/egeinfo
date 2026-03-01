from re import *
file = open(r"D:\Study\egeinfo\tests\4\24-2__63h4e.txt").readline()
num = "([1-4]+)"
pattern = f"([A]{num})([*+]{num})+"

mx = 0
for i in finditer(pattern, file):
    i = i.group()
    mx = max(mx, len(i))
print(mx)