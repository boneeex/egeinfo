from string import printable

alp = printable[:23]
for x in alp:
    exp = int(f"372{x}2145", 23) + int(f"62{x}112", 23)
    if exp % 22 == 0:
        print(exp / 22)