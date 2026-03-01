file = open(r"D:\Study\egeinfo\tests\4\5__1fsqj.csv")
matrix = [list(map(int, line.split(";"))) for line in file]

i, j = 19, 19
curr = 0            
def climb(i, j):
    up = matrix[i - 1][j]
    left = matrix[i][j - 1]
    if 