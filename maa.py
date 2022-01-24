from turtle import*
def mov(x,y):
     penup()
     goto(x,y)
     pendown()
mov(-300,200)
width(30)
circle(-50,-180)
fd(-600)
circle(50,-180)

mov(-150,100)
right(90)
fd(350)
circle(-60,270)
fd(270)
left(90)
fd(280)
back(380)

mov(150,100)
lt(180)
fd(390)

mov(0,200)
circle(90,180)

mov(90,170)
fd(1)

exitonclick()
