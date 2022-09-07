from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

pad1 = Paddle((370, 0))
pad2 = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=pad1.move_up)
screen.onkey(key="Down", fun=pad1.move_down)
screen.onkey(key="w", fun=pad2.move_up)
screen.onkey(key="s", fun=pad2.move_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_init()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    if (ball.distance(pad1) < 50 and ball.xcor() > 340) or (ball.distance(pad2) < 50 and ball.xcor() < -340):
        ball.bounce_pad()

    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_scorer()
    elif ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_scorer()

screen.exitonclick()
