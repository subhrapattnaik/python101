"""the turtle screen has a method called ontimer() that allows code to be called after a delay.

ontimer() takes two parameters.

    The first parameter is function you want to perform
    The second is the time (in milliseconds) before the function will be called. A value of 1000 is equal to a delay of 1 second.

The ontimer() method also requires that the screen object's listener be activated, so you need to call the listen() method at the end of 
your code."""

#The example below defines a function called change_color(). Its task is to change the screen color after 3 seconds.

import turtle
screen = turtle.Screen()

def change_color():
    screen.bgcolor("#123456")

screen.ontimer(change_color, 3000)
screen.bgcolor("#654321")

#---------------------------------------------------------------------
