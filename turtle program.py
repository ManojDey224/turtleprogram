import turtle
loadWindow= turtle.Screen()
turtle.bgcolor("black")
turtle.color("white")
turtle.pensize(1)
turtle.speed(5)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)