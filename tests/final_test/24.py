file = open(r"D:\Study\egeinfo\tests\final_test\24__7h77f.txt").readline()
start = mx = c = d = 0
for end in range(len(file)):
    if file[end] == "C":
        c += 1
    if file[end] == "D":
        d += 1

    while c > 2 or d > 2:
        if file[start] == "C":
            c -= 1
        if file[start] == "D":
            d -= 1
        start += 1

    mx = max(mx, end - start + 1)
print(mx)