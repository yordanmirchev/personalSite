import random
from turtle import Turtle

from constants import COLORS, SCREEN_WIDTH, BUFFER, SCREEN_HEIGHT


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.active_cars = []

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(int(SCREEN_WIDTH / 2) - BUFFER,
                 random.randint(-int(SCREEN_HEIGHT / 2) + 2 * BUFFER, int(SCREEN_HEIGHT / 2) - BUFFER))
        self.active_cars.append(car)

    def move_car(self, move_distance):
        for car in self.active_cars:
            car.setx(car.xcor() - move_distance)
