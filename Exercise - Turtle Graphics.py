# Turtle Graphics Exercise
# Author: Richard Flores
# Date: 3.11.23

from turtle import Turtle
from turtle import Screen

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

for _ in range(25):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()




screen = Screen()
screen.exitonclick()