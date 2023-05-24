import turtle, math

screen = turtle.Screen()

def make_a_star():
    # this is the radius of the star
    radius = 25
    # the arc to rotate by so you cover 2pi or 360 degrees in 10 steps
    inc = math.pi/5
    # start the rotation from pointing stright downward
    degree = -math.pi/2
    points = []
    
    # rotate 10 times
    for i in range(10):
        # alternate between 2/5 radius and radius as the length
	    if(i % 2):
		    length = radius
	    else:
		    length = 2*radius/5

	    # record each of the points
	    points.append((math.cos(degree)*length, math.sin(degree)*length))
	    degree+=inc
        
    return points

screen.register_shape('star', make_a_star())

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.shape("star")

