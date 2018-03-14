from turtle import *
shape('turtle')
color('blue')
speed(-1)

for i in range(24):
    for j in range(4):
        forward(100)
        left(90)
    left(360/24)

ht()

mainloop()
