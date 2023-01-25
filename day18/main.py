import turtle
from turtle import Turtle, Screen
import random as r

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.shape("turtle")
tim.color("green")


def draw_rectangle():
    for _ in range(0, 4):
        tim.left(90)
        tim.forward(150)


def draw_punctured_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_triangle():
    for i in range(3):
        tim.forward(20)
        tim.right(120)
        tim.forward(10)

def set_random_color():
    """Need to have screen color mode to 255 for the turtle module """
    tim.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))

def draw_n_angle_shape(n, size):
    if n < 3:
        n = 3
    set_random_color()
    for i in range(n):
        tim.forward(size)
        tim.right(360 / n)
        tim.forward(size)


def draw_multiple_colored_figrures(sides, size):
    for n in range(3, sides):
        draw_n_angle_shape(n, size)


def random_walk(steps, cycles, fixed_angle):
    tim.shape("circle")
    tim.pensize(15)
    tim.speed((7))
    for _ in range(cycles):
        set_random_color()

        if not fixed_angle:
            angle = r.randint(0,360)
        else:
            angle = 90

        position = ["left", "right"]
        direction = r.choice(position)
        if direction == "left":
            tim.left(angle)
        elif direction == "right":
            tim.right(angle)
        tim.forward(steps)


def draw_spirograph_v1():
    tim.speed(10)
    for i in range(0,360,10):
        set_random_color()
        tim.right(i)
        tim.circle(100)

def draw_spirograph_v2(size_of_gap):
    tim.speed(10)
    for i in range(0, int(360/size_of_gap)):
        set_random_color()
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)



#draw_rectangle()
#draw_punctured_line()
#draw_triangle()
#draw_multiple_colored_figrures(sides=15, size=20)
#random_walk(steps=20, cycles=100,fixed_angle=True)
#random_walk(steps=20, cycles=100,fixed_angle=False)
#draw_spirograph_v1()
draw_spirograph_v2(5)

screen.exitonclick()
