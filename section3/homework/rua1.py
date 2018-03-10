from turtle import *
shape('turtle')
speed(-1)

j = 3
for i in ['red', 'blue', 'brown', 'yellow', 'grey']:
    color(i)
    for k in range(j):
        forward(100)
        left(180-((j-2)*180/j))
    home()
    j +=1

mainloop()
