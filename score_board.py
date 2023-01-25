from turtle import Turtle
from data_manager import read_high_score_as_int, write_high_score
from constants import SCREEN_HEIGHT, ALIGN, FONT, BUFFER_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = read_high_score_as_int()
        self.write_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, int(SCREEN_HEIGHT / 2 - BUFFER_FONT))
        self.write(arg=f"Current score: {self.score}. High score: {self.high_score}", align=ALIGN, font=FONT)

    def write_end_game(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.high_score)
        self.score = 0
        self.update_score()
