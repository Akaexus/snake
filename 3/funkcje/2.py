import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(100)

def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)
size = 20

for i in range(5):
    square(size)
    size += 20
    t.penup()
    t.forward(-10)
    t.right(-90)
    t.forward(10)
    t.right(90)
    t.pendown()

wn.exitonclick()