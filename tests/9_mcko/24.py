file = open(r"D:\Study\egeinfo\tests\9_mcko\1001_24.txt").readline()
while "0" in file or "2" in file or "4" in file or "6" in file or "8" in file:
    file = file.replace("0", "*").replace("2", "*").replace("4", "*").replace("6", "*").replace("8", "*")

file = file.split("*")
mx = 0

def point(line):
    start = mx = q = 0
    for end in range(len(line)):
        if line[end] == "Q":
            q += 1

        while q > 50:
            if line[start] == "Q":
                q -= 1
                
            start += 1
        
        if q == 50:
            mx = max(mx, end - start + 2)
    return mx

for line in file:
    mx = max(mx, point(line))
    
print(mx)