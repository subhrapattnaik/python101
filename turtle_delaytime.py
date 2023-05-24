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


#n this example, we are going to make the square turtle teleport to a random location of the screen every second.
import turtle, random

screen = turtle.Screen()

square = turtle.Turtle()
square.shape("square")
square.penup()
square.speed(0)

def f():
    x = random.randint(-200, 200) # get a random number between -200 and 200
    y = random.randint(-200, 200)
    square.goto(x, y)
    screen.ontimer(f, 1000) # call f again after 1 second

screen.ontimer(f, 1000)
screen.listen()
