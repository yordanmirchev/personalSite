from turtle import Turtle
from random import randint

from constants import BUFFER, SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(- int(SCREEN_WIDTH / 2 - BUFFER), int(SCREEN_WIDTH / 2 - BUFFER)),
                  randint(- int(SCREEN_HEIGHT / 2 - BUFFER), int(SCREEN_HEIGHT / 2 - BUFFER)))
