from turtle import *
shape('turtle')
speed(-1)
color('red')
a = 30
for i in range(4):
    left(a)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    home()
    a = a+90
mainloop()
