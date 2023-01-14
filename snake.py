import time
from turtle import Turtle

from constants import INITIAL_POSITIONS, STEP_SIZE, LEFT, RIGHT, DOWN, UP, DISPLAY_DELAY, SPEED_UP_FACTOR


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.build_initial_body()
        self.head = self.snake_parts[0]

    def add_segment(self, possition):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.setposition(possition)

        self.snake_parts.append(t)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def build_initial_body(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def move(self):
        time.sleep(DISPLAY_DELAY)
        for segment in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[segment - 1].xcor()
            new_y = self.snake_parts[segment - 1].ycor()
            self.snake_parts[segment].goto(new_x, new_y)
        self.head.forward(STEP_SIZE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def speed_up(self):
        global DISPLAY_DELAY
        DISPLAY_DELAY *= SPEED_UP_FACTOR
