from turtle import Screen

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BUFFER, COLLISION_BUFFER
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def wall_is_reached():
    return snake.head.xcor() >= int(SCREEN_WIDTH / 2 - BUFFER) or snake.head.xcor() <= - int(
        SCREEN_WIDTH / 2 - BUFFER) or snake.head.ycor() >= int(
        SCREEN_HEIGHT / 2 - BUFFER) or snake.head.ycor() <= - int(SCREEN_HEIGHT / 2 - BUFFER)


def body_is_collided():
    for element in snake.snake_parts[1:]:
        if snake.head.distance(element) < COLLISION_BUFFER:
            return True
    else:
        return False


def play():
    game_is_on = True

    while game_is_on:
        screen.update()
        snake.move()

        if snake.head.distance(food) < BUFFER:
            food.refresh()
            snake.speed_up()
            score_board.update_score()

        if wall_is_reached() or body_is_collided():
            game_is_on = False
            score_board.write_end_game()


play()

screen.exitonclick()
