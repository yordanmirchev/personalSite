from turtle import Turtle
from constants import PADDLE_STARTING_X, PADDLE_STARTING_Y, PADDLE_STEP


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        if self.position == "left":
            self.setx(-PADDLE_STARTING_X)
        else:
            self.setx(PADDLE_STARTING_X)
        self.sety(PADDLE_STARTING_Y)



    def up(self):
        self.goto(self.xcor(), self.ycor() + PADDLE_STEP)

    def down(self):
        self.goto(self.xcor(), self.ycor() - PADDLE_STEP)
