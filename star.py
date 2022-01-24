import turtle
star= turtle.Turtle()
turtle.speed(5)
turtle.bgcolor('blue')
turtle.color("white")
turtle.pensize(19)
for x in range(240):
    star.forward(x)
    star.right(144)
    