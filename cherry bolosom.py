import turtle as T
import random
import time

# Draw the torso of cherry blossoms (60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # White
            else:
                t.color('lightcoral')  # Light coral
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # Light coral
            t.pensize(branch / 2)
        else:
            t.color('sienna')  #  (zhě) 
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# Falling petals
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # Light coral
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# Drawing area
t = T.Turtle()
# Canvas size
w = T.Screen()
t.hideturtle()  # Hide brush
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat wheat
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# Draw the torso of cherry blossoms
Tree(60, t)
# Falling petals
Petal(200, t)
w.exitonclick()