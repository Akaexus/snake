import turtle

sides = int(input('sides> '))
length = int(input('length> '))
sideColor = input('sideColor> ')
color = input('color> ')

wn = turtle.Screen()
t = turtle.Turtle()

def shape(sides, length, sideColor, color):
    t.color(sideColor)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()

shape(sides, length, sideColor, color)
wn.exitonclick()