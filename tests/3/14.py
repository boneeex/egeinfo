from string import printable
alp = printable[:21]

for x in alp:
    reg = int(f"2496{x}2", 21) + int(f"8{x}223", 21) + int(f"2331768{x}3", 21)
    if reg % 20 == 0:
        print(reg // 20)
        break