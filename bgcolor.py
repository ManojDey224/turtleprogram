import turtle
turtle.color("red")
turtle.bgcolor("blue")
turtle.pensize(10)
for angle in range(0,360,30):
    turtle.seth(angle)
    turtle.circle(100)