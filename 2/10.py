import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor('lightgreen')
t.speed(5)
t.color('blue')
for i in range(12):
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
    t.stamp()
    t.forward(-120)
    t.right(360/12)
wn.exitonclick()