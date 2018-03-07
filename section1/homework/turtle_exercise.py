from turtle import *
shape('turtle')
speed(-1)
color('blue')

fillcolor('yellow')
begin_fill()
for i in range(4):
    left(90)
    forward(100)

penup()
goto(100,0)
pendown()

for i in range(3):
    forward(120)
    left(120)

penup()
home()
goto(-50,-200)
pendown()
circle(50)

end_fill()

penup()
goto(125,-150)
pendown()

for i in range(8):
    circle(25)
    left(360/8)

penup()
goto(300,-150)
pendown()

for i in range(30):
    circle(25)
    left(360/30)

ht()
mainloop()
