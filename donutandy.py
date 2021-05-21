from turtle import Screen
import turtle

from random import *
molly = turtle.Turtle()
molly.speed(20)
jeff = turtle.Turtle()
dav = turtle.Turtle()
turtle.screensize(canvwidth=2000, canvheight=2000, bg=None)
jeff.speed(20)
dazv = turtle.Turtle()
dazv.speed(20)
met = turtle.Turtle()
met.speed(20)
jack = turtle.Turtle()
jack.speed(20)
x = 10000


dav.speed(20)
def lmao():



        jeff.forward(10)
        jeff.right(45)
        jeff.circle(100)
        jeff.forward(-60)
        jeff.back(29)
        jeff.left(23)
        jeff.back(29)
 

        jack.forward(-10)
        jack.right(-45)
        jack.circle(100)
        jack.forward(60)
        jack.back(-29)
        jack.left(-23)
        jack.back(-29)

  
        met.forward(10)
        met.right(45)
        met.circle(100)
        met.forward(-60)
        met.back(29)
        met.left(23)
        met.back(29)
       


        dav.forward(-10)
        dav.right(-45)
        dav.circle(100)
        dav.forward(60)
        dav.back(-29)
        dav.left(-23)
        dav.back(-29)
      



        
met.up()
met.right(90)
met.forward(10)
met.down()
dav.up()
dav.right(-90)
dav.forward(-10)
dav.down()
color = 10
while True:
    
    lmao()
    color = color + 1
    print(color)
    mod = color % 2
    if mod > 0: 
        jeff.pencolor("blue")
        met.pencolor("blue")
        jack.pencolor("blue")
        dav.pencolor("blue")
        pass
    else:
        jeff.pencolor("red")
        jack.pencolor("red")
        dav.pencolor("red")
        met.pencolor("red")
        pass
