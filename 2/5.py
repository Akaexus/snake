import turtle
wn = turtle.Screen()
t = turtle.Turtle()

def shape(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)

shape(3)
shape(4)
shape(6)
shape(8)

wn.exitonclick()