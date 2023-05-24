import turtle

def create_turtle(x, y):
    t = turtle.Turtle()
    t.shape("square")
    t.penup()
    t.speed(0)
    t.goto(x,y)

create_turtle(0,0)
create_turtle(100,0)
create_turtle(0,100)
#\
#----------------------------------------------
#\
"""
if we want to make games, we need a way to detect and respond to key presses 
in your programs so that the player can control the game.
syntax:
screen.onkey(func_name, "key")

\

screen.onkey(jump, "Space")

For example, you might define a function called jump(), then bind the Space key to that function. You'd write that like this:

----------------------------------------------------------------"""
"""

Listen for Keys

Once you've used onkey(), we have to add another line of code to activate the turtle screen's listener. Otherwise, the screen won't "hear" the keys being pressed. You use it like this:

screen.listen()

Notice that the listen() method does not require a parameter, and you only need to call it once to activate a turtle screen's listener, even if you have more than one onkey() method.

----------------------------------------"""
