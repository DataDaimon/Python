# Turtle Spirograph
# Author: Richard Flores
# Date: 3.15.23

import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

heading = 10

for _ in range(0, 36):
    tim.circle(100)
    tim.setheading(heading)
    tim.color(random_color())
    heading += 10



screen = Screen()
screen.exitonclick()