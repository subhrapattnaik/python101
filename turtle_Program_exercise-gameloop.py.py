"""The code below currently creates a single sprite using the create_turtle() command. Modify the code to create multiple sprites using clone(),
and move each clone to a different location while also giving it a different color."""


import turtle

t = turtle.Turtle()
t.shape("square")
t.penup()
t.speed(0)


actor1 = t.clone()
actor1.color("blue")
actor1.showturtle()
actor1.goto(-100,170)

actor2 = t.clone()
actor1.color("red")
actor2.showturtle()
actor2.goto(100,170)

#----------------------------------------
""""What Are Game Loops?

Most games consist of a series of steps that are repeated constantly as the game is played.

These steps often include tasks like:

    Setting and updating all the sprites (their location, whether to show or hide each sprite, and so forth)
    Checking on important conditions (such as whether the game has been won or lost)
"""
"""
Game Loop Basics

We can implement a game loop using a timer. You'll use an update function that sets a timer that calls itself in the future. This creates a cycle in which the update() function is called again and again, on a regular interval. This process of a function calling itself is a concept called recursion. This is the big idea behind the game loop.

You'll need to call the update() function for the first time to kick off the cycle.


this example is similar to the previous one, except the update() function now switches the background to a random color every second.

Press Run and see the background switch color.
"""

import turtle, random
screen = turtle.Screen()

def update():
    screen.bgcolor("#" + str(random.randint(0,800080)))
    screen.ontimer(update, 1000)

update()

#--------------------------------------------------


#Perform actions with the sprite in the game loop to do something interesting. Need ideas? You might change the pen's color, clone a sprite, or change the shape of a sprite.

import turtle, random
screen = turtle.Screen()

sprite = turtle.Turtle()
#sprite.penup()
sprite.speed(0)
#sprite.st()

def update():
    #Add code for the turtle here
    #sprite.color("#" + str(random.randint(0,800080))
    screen.bgcolor("#" + str(random.randint(0,800080)))
    screen.ontimer(update, 1000)
#Call update here
update()
