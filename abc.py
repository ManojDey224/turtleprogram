import turtle
import math
anms=turtle.Turtle()
anms.color("red","black")
anms.speed(1000)
anms.pensize(3)
anms.shape('turtle')
anms.begin_fill()
for i in range(2000):
     anms.forward(math.sqrt(i))
     anms.left(i% 190)

anms.end_fill()

turtle.mainloop()
