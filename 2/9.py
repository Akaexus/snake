import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(20)

for i in range(5):
    t.forward(200)
    t.left(180-36)


wn.exitonclick()