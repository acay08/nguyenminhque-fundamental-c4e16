from turtle import *
shape('turtle')
speed(-1)
color('purple')

a = 5
for i in range(100):
    forward(a)
    left(90)
    a +=5
penup()
home()
mainloop()
