#Plotting A Parabola

Now that you get the idea, let's see another function. The code below will graph a parabola:

import turtle, math

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("green")

# loop through the domain
for i in range(-100,100) : 
    
    # define x in terms of i
    x = i/10.0 

    # define y in terms of x (our parabola function)
    y = x**2 - 100
    

    # check if y is a number, then goto(x,y)
    if(not math.isnan(y)) : 
        pen.goto(x, y)
        pen.pendown()
