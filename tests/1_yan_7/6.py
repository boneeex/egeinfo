from turtle import *
left(90)
tracer(0)
m = 7
screensize(5000, 5000)

right(315)

for _ in range(7):
    forward(72 * m)
    right(45)
    forward(43 * m)
    right(135)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(2)

done()