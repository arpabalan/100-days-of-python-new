from random import randint
from turtle import Screen,Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# -290 to 280
class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            timmy = Turtle()
            random_color = randint(0, 5)
            random_car_y_position = randint(-250, 250)
            random_car_x_position = randint(290, 1500)
            timmy.penup()
            timmy.color(COLORS[random_color])
            timmy.setheading(-180)
            timmy.shape("square")
            timmy.shapesize(1,2)
            timmy.goto(random_car_x_position, random_car_y_position)
            self.car_list.append(timmy)

    def car_move(self):
        for car in range(1,len(self.car_list)):
            self.car_list[car].forward(STARTING_MOVE_DISTANCE)








