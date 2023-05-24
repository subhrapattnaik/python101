import turtle
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

for i in range(len(shapes)):
    sprite = turtle.Turtle()
    sprite.penup()
    sprite.speed(0)
    sprite.shape(shapes[i])
    sprite.goto(-100+i*40,0)
