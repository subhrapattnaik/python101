#More Graphing with Turtle

#Let's try to make some more beautiful graphs!

#You can create more complex graphs using parametric functions. 

#Even if you haven't learned about parametric functions yet in math class, experiment with the code given and see what happens!


import turtle, math 

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("yellow")
for i in range(0,628) :
    t = i/50.0

    # draw a flower
    k = 6 
    x = 100*math.cos(k*t)*math.cos(t)
    y = 100*math.cos(k*t)*math.sin(t)
        
    if(not math.isnan(y)) :
        pen.goto(x, y)
        pen.pendown()
        
        
        #https://www.tynker.com/code/project/5ffddea3f8740573224b546b
        
        learn more about drawing different patterns by turtle
