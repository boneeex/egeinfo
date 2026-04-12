from turtle import *
m = 30
left(90)
tracer(0)

right(315)
for i in range(7):
    forward(12 * m)
    right(45)
    forward(6 * m)
    right(135)
up()
for x in range(-70, 70):
    for y in range(-70, 70):
        goto(x * m, y * m)
        dot(5)
done()