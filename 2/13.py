import turtle

n = int(input())

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(20)

for i in range(n):
    t.forward(200)
    t.forward(-200)
    t.right(360/n)

wn.exitonclick()