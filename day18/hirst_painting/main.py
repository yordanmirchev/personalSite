import colorgram
import turtle
from turtle import Turtle, Screen
from random import choice

# TODO : Optimize code to make it clear

def extract_rgb_from_image(image_name, number_of_colors):
    """Returns a list of tuples for the rgb colors of the image"""
    colors = colorgram.extract(image_name, number_of_colors)
    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return rgb_colors;

#rgb_colors = extract_rgb_from_image('111.webp', 30);

#print(rgb_colors)
#print(rgb_colors)

## Set up variables
tim = Turtle()
screen = Screen()
turtle.colormode(255)
colors =[(249, 248, 247), (251, 248, 250), (241, 249, 245), (242, 245, 250), (239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50), (212, 127, 164), (34, 194, 117), (139, 183, 18), (189, 18, 39), (108, 105, 194), (232, 55, 45), (244, 147, 183), (113, 191, 149), (191, 46, 66), (19, 187, 206), (45, 52, 105), (136, 221, 240), (146, 229, 169), (202, 210, 7), (22, 151, 116), (233, 174, 159), (31, 43, 76), (112, 42, 40), (181, 178, 220), (80, 34, 37)]

def position_turtle():
    tim.hideturtle()
    tim.speed(10)
    tim.penup()
    tim.setx(-150)
    tim.sety(-150)
    tim.pendown()


def draw_row():
    for j in range(10):
        tim.dot(20, choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()


def draw_a_painting_vertical():
    position_turtle()

    for i in range(10):
        tim_x = tim.xcor()
        tim_y = tim.ycor()
        tim.setheading(90)
        draw_row()
        tim.penup()
        tim.setx(tim_x)
        tim.sety(tim_y)
        tim.pendown()
        tim.setheading(0)
        tim.dot(20, choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    screen.exitonclick()

def draw_a_painting_horizontal():
    position_turtle()
    for i in range(10):
        tim_x = tim.xcor()
        tim_y = tim.ycor()
        draw_row()
        tim.penup()
        tim.setx(tim_x)
        tim.sety(tim_y)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)
        tim.pendown()

    screen.exitonclick()

#draw_a_painting_vertical()
draw_a_painting_horizontal()