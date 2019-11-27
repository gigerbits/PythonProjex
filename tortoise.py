#logan cannon
#10/11/2019
#tortoise
import turtle

x = turtle.Pen()

x.hideturtle
x.color("lime")
x.speed(0)
x.width(2)
x.up()
x.setposition(-300,300)
x.down()
base = 80

x.begin_fill()
for i in range(2):
    for i in range(8):
        for i in range(4):
            
            x.forward(base)
            x.right(90)
            
        x.forward(base) 
    x.back(base*8)
    x.right(90)
    x.forward(base)
    x.left(90)
x.end_fill()
for i in range(2):
    x.begin_fill()
    for i in range(4):
        x.forward(base)
        x.right(90)
    x.end_fill()
    x.forward(base)
    x.color("black")
    x.begin_fill()
    for i in range(2):
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.forward(base)
    x.end_fill()

    x.color("lime")
    x.begin_fill()
    for i in range(2):
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.forward(base)
    x.end_fill()

    x.color("black")
    x.begin_fill()
    for i in range(2):
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.forward(base)
    x.end_fill()
    x.color("lime")
    x.begin_fill()
    for i in range(4):
        x.forward(base)
        x.right(90)
    x.forward(base)
    x.end_fill()
    x.up()
    x.back(base*8)
    x.right(90)
    x.forward(base)
    x.left(90)
    x.down()
for i in range(3):
    x.begin_fill()
    x.color("lime")
    for i in range(4):
        x.forward(base)
        x.right(90)
    x.end_fill()
    x.forward(base)
for i in range(2):
    x.color("black")
    x.begin_fill()
    for i in range(4):
        x.forward(base)
        x.right(90)
    x.end_fill()
    x.forward(base)
for i in range(3):
    x.begin_fill()
    x.color("lime")
    for i in range(4):
        x.forward(base)
        x.right(90)
    x.end_fill()
    x.forward(base)
x.up()
x.back(base*8)
x.right(90)
x.forward(base)
x.left(90)
x.down()
for i in range(2):
    for i in range(2):
        x.begin_fill()
        x.color("lime")
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)
    for i in range(4):
        x.color("black")
        x.begin_fill()
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)
    for i in range(2):
        x.begin_fill()
        x.color("lime")
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)
    x.up()
    x.back(base*8)
    x.right(90)
    x.forward(base)
    x.left(90)
    x.down()
for i in range(2):
    for i in range(2):
        x.begin_fill()
        x.color("lime")
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)
    for i in range(1):
        x.color("black")
        x.begin_fill()
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)
for i in range(2):
        x.begin_fill()
        x.color("lime")
        for i in range(4):
            x.forward(base)
            x.right(90)
        x.end_fill()
        x.forward(base)







##y = turtle.Pen()
##y.color("red")
##y.speed(0)
##for i in range(1000):
##    y.forward(3*i)
##    y.left(1*i)
##    
##    
