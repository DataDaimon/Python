# Turtle Graphics Exercise
# Author: Richard Flores
# Date: 3.11.23

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

# 360 divided by number of sides

sides = 3
colors = ['blue', 'red', 'yellow', 'green', 'purple', 'pink', 'brown']

def angle(sides):
    angle = 360 / sides
    return angle

def draw_shape(sides):
    for _ in range(0, sides):
        tim.forward(100)
        tim.right(angle(sides))

for _ in range(sides, 10):
    draw_shape(sides)
    sides += 1
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()