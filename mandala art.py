import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("yellow")
t.pencolor("blue")
t.pensize(0)
t.speed(0)
c=0
d=0
while True:
    for i in range(7):
        t.forward(140)
        t.right(80)
        t.right(5)
        c+=1
        if c>=390/15:
            t.forward(50)
            c = 0
            d +=1
        if d>=12:
                break
        t.hideturtle()
        