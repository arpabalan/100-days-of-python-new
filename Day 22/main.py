from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
PADDLE_RIGHT_POSITION = (350,0)
PADDLE_LEFT_POSITION = (-350,0)



screen = Screen()
screen.title('Pong Game')
screen.bgcolor("black")
screen.setup(width=800, height=600)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.score_board()
scoreboard.update_scoreboard()
is_on = True

right_paddle = Paddle()
right_paddle.create_paddle(PADDLE_RIGHT_POSITION)

left_paddle = Paddle()
left_paddle.create_paddle(PADDLE_LEFT_POSITION)
ball.ball()


while is_on:
    screen.update()
    time.sleep(ball.speed)
    ball.ball_movement_y()
    ball_distance_upper_wall = 300 - ball.ycor()
    ball_distance_lower_wall = -300 - ball.ycor()
    if ball_distance_upper_wall < 50 or ball_distance_lower_wall > -50:
        ball.bounce_y()

    if ball.distance(right_paddle) < 30 and ball.xcor() > 285:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 30 and ball.xcor() < -285:
        ball.bounce_x()
        ball.speed  *= 0.9

    if ball.xcor() < -400:
        ball.reset()
        ball.ball()
        scoreboard.r_point()

    if ball.xcor() > 400:
        ball.reset()
        ball.ball()
        ball.bounce_x()
        scoreboard.l_point()







    screen.listen()
    screen.onkey(key="Up",fun=right_paddle.paddle_up)
    screen.onkey(key="Down", fun=right_paddle.paddle_down)
    screen.onkey(key="w",fun=left_paddle.paddle_up)
    screen.onkey(key="s", fun=left_paddle.paddle_down)



screen.exitonclick()