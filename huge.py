import turtle
x = 2
import time
turtle.speed(20)
turtle.screensize(canvwidth=6000, canvheight=3380, bg=None)



while True:
    turtle.forward(60)
    turtle.right(x)
    x = x + 1
    if x > 200:
        turtle.forward(20)
        turtle.left(20)
        turtle.back(2)

    
