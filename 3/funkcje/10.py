import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(100)

def pentagram(size, n):
    for i in range(5):
        t.forward(size)
        t.right(144)

for i in range(5):
    t.penup()
    t.forward(350)
    t.pendown()
    pentagram(100)
    t.penup()
    t.right(144)

wn.exitonclick()