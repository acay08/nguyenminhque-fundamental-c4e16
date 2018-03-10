from turtle import *
shape('turtle')
speed(-1)

for i in ['red', 'blue', 'brown', 'yellow', 'grey']:
    color(i,i)
    begin_fill()
    for k in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    penup()
    forward(50)
    pendown()

mainloop()
