Define Your Own Shape

You can also create your own shape by registering a list of points with the screen object:
  
  import turtle
screen = turtle.Screen()
points = [(-20,-20),(20,-20),(20,0),(0,0),(0,20),(-20,20)]
screen.register_shape('new', points)

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.shape("new")
