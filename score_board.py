from turtle import Turtle

from constants import SCREEN_HEIGHT, ALIGN, FONT, BUFFER_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, int(SCREEN_HEIGHT / 2 - BUFFER_FONT))
        self.write(arg=f"Current score: {self.score}", align=ALIGN, font=FONT)

    def write_end_game(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)
