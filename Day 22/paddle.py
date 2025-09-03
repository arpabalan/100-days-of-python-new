from turtle import Turtle


PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

class Paddle(Turtle):
    def __int__(self):
        super().__int__()


    def create_paddle(self, PADDLE_POSITION):
        self.goto(PADDLE_POSITION)
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def paddle_up(self):
        self.penup()
        self.setheading(90)
        self.forward(20)

    def paddle_down(self):
        self.penup()
        self.setheading(90)
        self.backward(20)

