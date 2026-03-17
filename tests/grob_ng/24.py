from re import *
file = open(r"D:\informaticsclass\egeinfo\tests\grob_ng\24.txt").readline()

pattern = "([\)][0-9A-Z\(])"
sm = 0
mx = 0
goal = 0
for i in range(len(file)):
    while i != goal:
        continue