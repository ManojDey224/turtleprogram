import turtle
wn=turtle.Screen()
wn=turtle.bgcolor("black")
tr=turtle.Turtle()
move=1
tr.speed("fastest")
for i in range (360):
    tr.pendown()
    tr.color("Violet")
    tr.right(move)
    tr.forward(100)
    tr.circle(10)
    tr.penup()
    tr.color("orange")
    tr.pendown()
    tr.right(30)
    tr.forward(60)
    tr.pendown()
    tr.color("red")
    tr.left(200)
    tr.forward(50)
    tr.right(70)
    tr.penup()
    tr.color("Brown")
    tr.pendown()
    tr.forward(70)
    tr.circle(20)
    tr.penup()
    tr.home()
    move=move+1
tr.penup()
tr.forward(50)
tr.pendown()
for i in range (360):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    tr.pendown()
    tr.color("Violet")
    tr.right(move)
    tr.forward(100)
    tr.circle(10)
    tr.penup()
    tr.color("orange")
    tr.pendown()
    tr.right(30)
    tr.forward(60)
    tr.pendown()
    tr.color("red")
    tr.left(30)
    tr.forward(30)
    tr.penup()
    tr.home()
    move=move+1