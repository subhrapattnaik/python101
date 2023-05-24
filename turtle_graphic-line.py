#Graphing A Line

#Let's say we wanted to draw a simple line, the kind that you have seen in math class—described by a function that looks like this: y = mx + b

#Here's how we could get the turtle to graph a function like that. Write the code and press Play to watch it draw the line. 


import turtle, math

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("blue")

# loop through the domain
for i in range(-100,100) : 
    
    # define x in terms of i
    x = i/10.0
    
    # define y in terms of x 
    y = 2*x + 3
    
    # check if y is a number, then goto(x, y)
    if(not math.isnan(y)) :
        pen.goto(x, y)
        pen.pendown()
