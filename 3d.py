import turtle as t
t.bgcolor('black')
t.color('yellow')
t.speed(11)
for i in range(150):
     t.circle(30)
     if 7<i<62:
          t.left(5)
     if 80<i<133:
          t.right(5)
     if i<80:
          t.forward(10)
     else:
          t.forward(5)

t.done()
