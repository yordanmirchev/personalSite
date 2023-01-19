import time
from turtle import Turtle, Screen
from player import Player

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_DELAY

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race")
screen.tracer(0)

player = Player()
game_is_on = True

while game_is_on:
    time.sleep(DISPLAY_DELAY)
    screen.update()

screen.exitonclick()
