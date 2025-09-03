from turtle import Turtle, Screen
import time


FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_level()
    def update_level(self):
        self.write(f"LEVEL {self.current_level}", False, align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", True, align="center", font=FONT)


    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_level()

