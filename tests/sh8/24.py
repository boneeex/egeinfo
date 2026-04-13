file = open(r"D:\informaticsclass\egeinfo\tests\sh8\24 (1).txt").readline()
while "A" in file or "E" in file or "I" in file or "O" in file or "U" in file or "Y" in file:
    file = file.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*").replace("Y", "*")

mn = 10 ** 7
for line in file.split("*"):
    z = 0
    line = line[::-1]
    for idx, i in enumerate(line):
        if i == "Z":
            z += 1
        if z == 72:
            mn = min(mn, idx + 2)
            break
print(mn)