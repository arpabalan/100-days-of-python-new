import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


current_level = 0
screen = Screen()

screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
car = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)
screen.onkey(key="Down", fun=player.move_down)

level_speed = 1

while game_is_on:
    time.sleep(0.1 * level_speed)
    screen.update()
    car.create_car()
    car.car_move()

    if player.ycor() >= 260:
        scoreboard.increase_level()
        player.refresh()
        level_speed *= .5

    for car_distance in car.car_list:
        if car_distance.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False








screen.exitonclick()




