# Turtle Graphics Exercise
# Author: Richard Flores
# Date: 3.11.23

from turtle import Turtle
from turtle import Screen

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

for _ in range(4):
    tim.forward(100)
    tim.left(90)


screen = Screen()
screen.exitonclick()