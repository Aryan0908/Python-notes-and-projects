import turtle

import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("hirst_spot_painting.jpg", 34)
colors_rgb = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35),
              (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64),
              (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79),
              (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171),
              (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204), (78, 66, 42),
              (23, 99, 96)]

# for color_num in range(0, len(colors)):
#     r = colors[color_num].rgb[0]
#     g = colors[color_num].rgb[1]
#     b =  colors[color_num].rgb[2]
#     rgb = (r, g, b)
#     colors_rgb.append(rgb)
#
# print(colors_rgb)

timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()


def random_rgb(color_list):
    return random.choice(color_list)


def timmy_position(x, y):
    return timmy.goto(x, y)


def drawing():
    for dots in range(10):
        timmy.dot(20, random_rgb(colors_rgb))
        timmy.penup()
        timmy.forward(50)


x_axis = -200
y_axis = -200
complete = 0

while complete < 10:
    timmy_position(x=x_axis, y=y_axis)
    drawing()
    y_axis += 50
    complete += 1

screen.exitonclick()
