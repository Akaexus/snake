import turtle
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

wn = turtle.Screen()
t = turtle.Turtle()
for angle in angles:
    t.forward(100)
    t.left(angle)

wn.exitonclick()

print(sum(angles) % 360)