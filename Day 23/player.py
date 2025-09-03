
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):


        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            self.forward(0)


    def move_left(self):
        self.goto((self.xcor()-MOVE_DISTANCE),self.ycor())

    def move_right(self):
        self.goto((self.xcor()+MOVE_DISTANCE),self.ycor())

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)