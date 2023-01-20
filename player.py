from turtle import Turtle
from constants import TURTLE_STARTING_X, TURTLE_STARTING_Y, TURTLE_STEP, SCREEN_HEIGHT, BUFFER


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_position()
        self.showturtle()


    def reset_position(self):
        self.goto(TURTLE_STARTING_X, TURTLE_STARTING_Y)

    def up(self):
        self.forward(TURTLE_STEP)

    def is_at_finish(self):
       return self.ycor() >= int(SCREEN_HEIGHT / 2) - BUFFER