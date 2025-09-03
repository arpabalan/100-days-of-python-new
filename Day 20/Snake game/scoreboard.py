from turtle import Turtle, Screen
import time
screen = Screen()
class Scoreboard(Turtle):

    def scoreboard_title(self,currentscore):

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,282)
        self.write(f"Score = {currentscore}", True, align="center", font=('Arial', 12, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", True, align="center", font=('Arial', 12, 'normal'))





