from turtle import Turtle
import time
from constants import DISPLAY_DELAY, BALL_STEP, SCREEN_WIDTH, SCREEN_HEIGHT, BUFFER, PADDLE_DISTANCE_BUFFER, \
    PADDLE_STARTING_X

diff_x = int(SCREEN_WIDTH / BALL_STEP)
diff_y = int(SCREEN_HEIGHT / BALL_STEP)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + diff_x
        new_y = self.ycor() + diff_y
        self.goto(new_x, new_y)
        time.sleep(DISPLAY_DELAY)

    def is_bound_reached(self):
        return self.ycor() >= SCREEN_HEIGHT / 2 - BUFFER \
            or self.ycor() <= -SCREEN_HEIGHT / 2 + BUFFER

    def bounce_y(self):
        new_x = self.xcor() + diff_x
        global diff_y
        diff_y *= -1
        new_y = self.ycor() + diff_y
        self.goto(new_x, new_y)
        time.sleep(DISPLAY_DELAY)

    def bounce_x(self):
        new_y = self.ycor() + diff_y
        global diff_x
        diff_x *= -1
        new_x = self.xcor() + diff_x
        self.goto(new_x, new_y)
        time.sleep(0.9*DISPLAY_DELAY)

    def is_paddle_reached(self, paddle):
        if paddle.position == "right":
            paddle_pos = PADDLE_STARTING_X - BUFFER
            return self.distance(paddle) < PADDLE_DISTANCE_BUFFER and self.xcor() > paddle_pos
        else:
            paddle_pos = - PADDLE_STARTING_X + BUFFER
            return self.distance(paddle) < PADDLE_DISTANCE_BUFFER  and self.xcor() < paddle_pos

    def left_missed(self):
        return self.xcor()< - int(SCREEN_WIDTH/2)
    def right_missed(self):
        return self.xcor() > int(SCREEN_WIDTH/2)
