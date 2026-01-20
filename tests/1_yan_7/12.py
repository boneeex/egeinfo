a = bin(321)[2:]
s = ""
for i in a:
    if i == "1":
        s += "0"
    else:
        s += "1"

print(int(s[s.find("1"):], 2))