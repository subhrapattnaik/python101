import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")

sprite = turtle.Turtle()

sprite.speed(1)
sprite.shape("arrow")
sprite.penup()
sprite.goto(-10,10)
sprite.pendown()
sprite.forward(100)
sprite.left(90)
sprite.forward(80)
sprite.right(90)
sprite.forward(100)
