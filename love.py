import turtle
window =turtle.Screen()
window.bgcolor("black")
turtle=turtle.Turtle()
turtle.shape("turtle")
turtle.color("yellow")
turtle.width(41)
turtle.speed(0)
colors=["yellow","red","orange","blue","green","purple"]
def heart():
    for blood in range(43):
        turtle.pencolor(colors[blood%9])
        turtle.right(5)
        turtle.forward(5)
        turtle.forward(150)
        turtle.penup()
        turtle.right(140)
        turtle.forward(147)
        turtle.pendown()
        for blood in range(43):
            turtle.pencolor(colors[blood%9])
            turtle.left(5)
            turtle.forward(5)
            turtle.left(7)
            turtle.forward(151)
        turtle.penup()
        turtle.left(90)
        turtle.forward(400)
        
        