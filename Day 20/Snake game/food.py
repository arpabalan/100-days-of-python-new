from random import randint
from turtle import Turtle, Screen
import random


class Food(Turtle):
    def food(self):
        super().__init__()
        self.shape("circle")

        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")

        self.refresh()


    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)

        self.goto(random_x, random_y)