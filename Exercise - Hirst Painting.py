# Hirst Painting
# Author: Richard Flores
# Date: 3.16.23

# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('Hirst.png', 10)
#
# color_tuple = []
#
# for n in range(0, 10):
#     first_color = colors[n]
#     rgb = first_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color_tuple.append((r,g,b))
import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (224, 137, 60), (196, 145, 171),
              (234, 226, 204), (225, 234, 231), (140, 178, 205), (139, 82, 105)]

tom = Turtle()

tom.hideturtle()
tom.penup()
tom.speed("fastest")
tom.goto(-225, -150)

for _ in range(0, 10):
    for _ in range(0,10):
        tom.color(random.choice(color_list))
        tom.dot(20)
        tom.forward(50)
    tom.backward(50)
    tom.setheading(90)
    tom.forward(50)
    tom.setheading(180)
    tom.forward(450)
    tom.setheading(0)


screen = Screen()
turtle.exitonclick()