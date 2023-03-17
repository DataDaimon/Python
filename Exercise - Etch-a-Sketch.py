# Etch-A-Sketch
# Author: Richard Flores
# Date: 3/17/2023

from turtle import Turtle, Screen

tieg = Turtle()
screen = Screen()

def move_forward():
    tieg.forward(10)

def move_backward():
    tieg.backward(10)

def move_clockwise():
    tieg.right(10)

def move_cclockwise():
    tieg.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_cclockwise)

screen.exitonclick()