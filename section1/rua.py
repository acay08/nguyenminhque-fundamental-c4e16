from turtle import *
shape('turtle')
speed(-1)
color('purple')


for i in range(20):
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)

    left(17)

penup()
for i in range(3):
    stamp()
    forward(50)
pendown()

for i in range(5):
    forward(100)
    left(180-36)

mainloop()
