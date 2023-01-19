from turtle import Turtle
from constants import TURTLE_STARTING_X, TURTLE_STARTING_Y


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(TURTLE_STARTING_X, TURTLE_STARTING_Y)
        self.showturtle()
