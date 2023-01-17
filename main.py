from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from turtle import  Screen
from paddle import  Paddle
from ball import  Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle(position = "left")
r_paddle = Paddle(position ="right")
screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
ball = Ball()
scoreboard = ScoreBoard()

#ball.goto(-100, 250)
endGame = True

while endGame:
 screen.update()
 ball.move()
 if ball.is_bound_reached():
  ball.bounce_y()
 if ball.is_paddle_reached(r_paddle) or ball.is_paddle_reached(l_paddle):
  ball.bounce_x()

 if ball.left_missed():
  scoreboard.rscore += 1
  scoreboard.update()
  ball = Ball()
  ball.bounce_x()

 if ball.right_missed():
  scoreboard.lscore += 1
  scoreboard.update()
  ball = Ball()
  ball.bounce_x()



screen.exitonclick()

