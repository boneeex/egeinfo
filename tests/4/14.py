from string import printable
alp = printable[:21]

for x in alp:
    exp = int(f"12{x}ac", 21) + int(f"90f{x}e", 21)
    if exp % 53 == 0:
        print(exp / 53)
        break