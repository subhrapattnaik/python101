import turtle, random
screen = turtle.Screen()
#--------------------------------------------

#Define the Ship and Asteroids


screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
#the '\' character indicates that the code wraps 
#and continues to the next line

screen.register_shape("rock1",((-20, -16),(-21, 0),(-20,18), \
                               (0,27),(17,15),(25,0),(16,-15),(0,-21)))
screen.register_shape("rock2",((-15, -10),(-16, 0),(-13,12), \
                               (0,19),(12,10),(20,0),(12,-10),(0,-13)))
screen.register_shape("rock3",((-10,-5),(-12,0),(-8,8),(0,13), \
                               (8,6),(14,0),(12,0),(8,-6),(0,-7)))
#------------------------------------------------
#Create the Ship

ship = turtle.Turtle()
ship.shape("ship")
ship.penup()
ship.speed(0)
ship.color("green")
#-------------------------------------------------
#Create the Asteroids


asteroids = []
for i in range(10) :
    a = turtle.Turtle()
    a.penup()
    a.speed(0)
    a.shape("rock" + str(random.randint(1,3)))
    a.goto(random.randint(-200,200),random.randint(-200,200))
    asteroids.append(a)
    
#----------------------------------------------
#Controlling The Ship 

def right() :
   
    ship.right(10)
                        
def left() :
    ship.left(10)
            
def forward() :
    ship.forward(5)
            
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(forward, "Up")
screen.listen()


#Press Play and move the ship around the asteroids. The game isn't complete but isn't it cool, anyway?!

"""here are some ideas for the game:

    Hide the ship with hideturtle() if it touches an asteroid.
    Every time the ship moves forward, loop through the list of asteroids.
    Create a function that shoots a bullet.

        Start by creating a shape and turtle for the bullet.
        Create a function that has the bullet go to the ship and then forward in the same direction as the ship.
        While the bullet is moving, check its location against all the asteroids by looping through the list."""

