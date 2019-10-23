import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(100)

def star(size, n):
    for i in range(n):
        t.forward(size)
        t.right(180 - 180/n)

star(100, 33)

wn.exitonclick()