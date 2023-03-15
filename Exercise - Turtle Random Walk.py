# Turtle Random Walk
# Author: Richard Flores
# Date: 3.15.23

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("blue")
tim.width(10)
tim.speed(4)

angles = (90, 180, 270, 360)
colors = ["red","blue","gray","green","yellow","orange","pink","purple"]

for _ in range(0, 100):
    tim.forward(40)
    tim.right(random.choice(angles))
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()