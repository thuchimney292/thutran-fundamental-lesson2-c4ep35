from turtle import *
color("blue")
pensize(2)
for i in range(3):
    forward(100)
    left(120)
for i in range(4,7):
    if i%2==0:
         color("red")
    else:
        color("blue")
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()