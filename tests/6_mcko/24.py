file = open(r"D:\Study\egeinfo\tests\6_mcko\1002_24.txt").readline()

while "0" in file or "2" in file or "4" in file or "6" in file or "8" in file:
    file = file.replace("0", "*")
    file = file.replace("2", "*")
    file = file.replace("4", "*")
    file = file.replace("6", "*")
    file = file.replace("8", "*")

file = file.split("*")

mn = 10 ** 7
for line in file:
    if line.count("Q") < 50:
        continue
    q = start = 0
    for end in range(len(line)):
        if line[end] == "Q":
            q += 1
        
        while q > 50:
            if line[start] == "Q":
                q -= 1
            start += 1
        if q == 50:
            mn = min(mn, end - line.find("Q") + 2)
print(mn)