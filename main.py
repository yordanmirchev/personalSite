import time
from turtle import Turtle, Screen

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, TURTLE_STARTING_X, TURTLE_STARTING_Y, DISPLAY_DELAY

turtle = Turtle()
turtle.hideturtle()
turtle.shape("turtle")
turtle.color("black")
turtle.penup()
turtle.setheading(90)
turtle.goto(TURTLE_STARTING_X, TURTLE_STARTING_Y)
turtle.showturtle()

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race")
screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(DISPLAY_DELAY)
    screen.update()

screen.exitonclick()
