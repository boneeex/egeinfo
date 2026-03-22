# https://education.yandex.ru/ege/inf/task/fda983ab-7199-45b9-878e-d56039b93aea
file = open(r"D:\Study\egeinfo\tests\profimatika1\26 (1).txt")
# 10000 - N
# 775 - K
batteries = sorted([int(line) for line in file])[::-1]
line = []
line.append(10**7)
print(line)
for battery in batteries:
    if line[0] - battery >= 775:
        line = [battery] + line
print(len(line) - 1, line[0])
