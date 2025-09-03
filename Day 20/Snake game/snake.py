import time
from turtle import Turtle,Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    segments = []
    def create_snake(self):
        for coordinate in STARTING_POSITION:
            self.add_segment(coordinate)


    def add_segment(self, coordinate):
        timmmy_the_turtle = Turtle()
        timmmy_the_turtle.color("white")
        timmmy_the_turtle.shape("square")
        timmmy_the_turtle.penup()
        timmmy_the_turtle.goto(coordinate)
        self.segments.append(timmmy_the_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def snake_movement_direction(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def move_right(self):
        if self.segments[0].heading() != LEFT:

            self.segments[0].setheading(RIGHT)
















