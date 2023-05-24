import turtle

screen = turtle.Screen() # get the Turtle Screen

screen.bgcolor("blue")

t = turtle.Turtle() #create a new turtle
t.shape("square")

t.forward(100)
t.goto(100, 0)
t.right(90)
t.forward(100)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.goto(-100,100)
t.pendown()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.color("red")
t.speed(5)
