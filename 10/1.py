file = open(r"D:\Study\egeinfo\10\1.txt", encoding="utf-8").read().lower()
file = file.replace("-то", 'то')
from re import *
pattern = "[а-я]?то[а-я]?"

cnt=0
for i in finditer(pattern, file):
    cnt += 1
print(cnt)