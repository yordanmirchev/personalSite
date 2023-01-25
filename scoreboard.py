from turtle import Turtle
from constants import FONT, SCREEN_WIDTH, SCREEN_HEIGHT


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-int(SCREEN_WIDTH/ 3), int(0.42 *SCREEN_HEIGHT))
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)


