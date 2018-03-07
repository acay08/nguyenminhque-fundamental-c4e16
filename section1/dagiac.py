socanh = int(input("ban muon hinh may canh?"))
from turtle import *
shape('turtle')
speed(-1)
color('purple')
fillcolor('blue')
begin_fill()
for i in range(socanh):
    forward(100)
    left(360/socanh)
end_fill()

mainloop()
