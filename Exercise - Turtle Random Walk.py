# Turtle Random Walk
# Author: Richard Flores
# Date: 3.15.23
import turtle
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.color("blue")
tim.pensize(15)
tim.speed(4)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

angles = (90, 180, 270, 360)

for _ in range(0, 100):
    tim.forward(40)
    tim.setheading(random.choice(angles))
    tim.color(random_color())

screen = Screen()
screen.exitonclick()