Create Your Own Custom Shape

Now you know how things work, create your own shape! You can move the turtle and record its position each time it moves to generate the points for a shape.



import turtle, math

screen = turtle.Screen()
sprite = turtle.Turtle()

# Complete the following custom_shape function to define your own shape!
def custom_shape():
    points = []
    points.append(sprite.pos())
    sprite.forward(10)
    points.append(sprite.pos())
    return points

screen.register_shape('custom', custom_shape())

sprite.penup()
sprite.speed(0)
sprite.shape('custom')
