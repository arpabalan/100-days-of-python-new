
from snake import Snake
from turtle import Turtle,Screen
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")

current_score = 0



screen.listen()
snake1 = Snake()
snake1.create_snake()
food = Food()
food.food()
scoreboard = Scoreboard()


screen.onkey(key="Down", fun=snake1.move_down)
screen.onkey(key="Left", fun=snake1.move_left)
screen.onkey(key="Right", fun=snake1.move_right)
screen.onkey(key="Up", fun=snake1.move_up)

is_on = True

while is_on:
    scoreboard.scoreboard_title(current_score)

    screen.update()
    time.sleep(0.001)
    snake1.snake_movement_direction()
    if snake1.segments[0].distance(food) < 15:
        snake1.extend()
        print("nom nom nom")
        current_score += 1
        scoreboard.clear()
        print(current_score)
        food.refresh()

    #wall collision detection
    if snake1.segments[0].xcor() > 270 or snake1.segments[0].xcor() < -270 or snake1.segments[0].ycor() > 270 or snake1.segments[0].ycor() < -270:
        scoreboard.game_over()
        is_on = False

    #tail collision detection
    for segment in snake1.segments[1::]:
        if snake1.segments[0].distance(segment) <10:
            is_on = False
            scoreboard.game_over()


screen.exitonclick()