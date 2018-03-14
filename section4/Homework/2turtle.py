from turtle import *
shape('turtle')
color('blue')
speed(-1)

fd = 1
for i in range(35):
    for j in range(4):
        forward(fd)
        left(90)
    left(15)
    fd += 2
ht()

mainloop()
