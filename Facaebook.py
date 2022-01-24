import turtle
from turtle import Screen

s = Screen()
s.bgcolor('white')

a = turtle.Turtle()
a.shape('arrow')
a.pensize(7)
a.color('blue')

a.begin_fill()
a.circle(140, 360)
a.end_fill()
a.right(7)
a.backward(32)
a.color('white')
a.pensize(3)
a.begin_fill()
a.left(97)
a.forward(98)
a.left(90)
a.forward(40)
a.right(90)
a.forward(40)
