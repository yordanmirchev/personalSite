import time
from turtle import Turtle, Screen
from player import Player
from carmanager import CarManager

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_DELAY, STARTING_MOVE_DISTANCE, BUFFER, MOVE_INCREMENT
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race")
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
scoreboard = ScoreBoard()

carmanager.create_car()
game_is_on = True
counter = 0;
moving_distance = STARTING_MOVE_DISTANCE;

while game_is_on:
    counter += 1;
    # Every 7 cycles of DISPLAY_DELAY we add a car , 0.7 sec
    if (counter % 7 == 0):
        carmanager.create_car()
    time.sleep(DISPLAY_DELAY)
    screen.update()
    screen.onkey(player.up, "Up")
    carmanager.move_car(moving_distance)

    for car in carmanager.active_cars:
        if player.distance(car) < BUFFER:
            print("Hit")
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        scoreboard.level += 1
        scoreboard.update()
        moving_distance += MOVE_INCREMENT
        player.reset_position()


screen.exitonclick()
