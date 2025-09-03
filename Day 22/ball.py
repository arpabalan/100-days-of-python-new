from sys import base_prefix
from turtle import Turtle



class Ball(Turtle):
    def __int__(self):
        super().__init__()


    def ball(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.new_x = 10
        self.new_y = 10
        self.speed = 0.1


    def ball_movement_y(self):
        new_x_cor = self.xcor() + self.new_x
        new_y_cor = self.ycor() + self.new_y
        self.goto(new_x_cor,new_y_cor)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1



