import turtle
x = 2
import time
turtle.speed(20)
turtle.screensize(canvwidth=6000, canvheight=3380, bg=None)

molly = turtle.Turtle()
molly.speed(20)
while True:
    turtle.forward(10)
    turtle.right(x)
    turtle.forward(-2)
    turtle.left(-20)
    turtle.back(-2)
    x = x + 1
    if x > 200:
        turtle.forward(2)
        turtle.left(20)
        turtle.back(2)


    molly.forward(-10)
    molly.right(-x)
    x = x + 1
    if x > 200:
        molly.forward(-2)
        molly.left(-20)
        molly.back(-2)
        molly.forward(2)
        molly.left(20)
        molly.back(2)    

    
