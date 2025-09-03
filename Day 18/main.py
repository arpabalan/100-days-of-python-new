


from random import randint, randrange, random
from turtle import Turtle, Screen
import turtle as t

color_pallet = [(252, 251, 248), (159, 180, 190), (219, 173, 125), (132, 74, 55), (52, 102, 151), (246, 233, 237), (118, 82, 93), (179, 140, 151), (161, 104, 151), (246, 251, 247), (44, 48, 67), (127, 173, 115), (84, 96, 182), (66, 11, 29), (239, 242, 247), (82, 133, 108), (230, 189, 139), (53, 62, 77), (193, 91, 74), (113, 45, 58), (94, 142, 119), (70, 66, 54), (183, 187, 205), (67, 61, 50), (207, 182, 191), (216, 181, 173), (178, 201, 177), (77, 59, 53), (174, 199, 203), (56, 66, 69)]
timmy_the_turtle = t.Turtle()
t.colormode(255)
timmy_the_turtle.shape("turtle")
turtle_colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue",
                 "LightSeaGreen","wheat","SlateGray","SeaGreen"
                 ]


class The_turtle():

    def __int__(self):
        pass
    timmy_the_turtle.hideturtle()


    def creating_square(self):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

    def drawing_dashes(self):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()

    def drawing_shapes(self, sides):
        area = 360
        shape_angle = area/sides
        for x in range(sides):
            timmy_the_turtle.color(turtle_colors[sides-3])
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(shape_angle)

    def walk(self):
        timmy_the_turtle.width(20)
        timmy_the_turtle.forward(30)
    def right_direction(self):
        timmy_the_turtle.right(90)
    def left_direction(self):
        timmy_the_turtle.left(90)
    def changing_line_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0,255)
        return timmy_the_turtle.pencolor(r,g,b)

    def hirst_color_pallet(self):
        random_number = randint(0, 29)
        random_color = color_pallet[random_number]
        red = random_color[0]
        green = random_color[1]
        blue = random_color[2]
        return timmy_the_turtle.pencolor(red,green,blue)

    def drawing_circle(self, gap_size):
        for x in range(int(360/gap_size)):
            self.changing_line_color()
            timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)
            timmy_the_turtle.circle(100)
            timmy_the_turtle.speed(0)
    def turtle_forward(self):
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
    def drawing_dot(self):
        self.hirst_color_pallet()
        timmy_the_turtle.dot(20)
    def turtle_position(self, y_position):
        timmy_the_turtle.penup()
        timmy_the_turtle.setposition(-150, y_position)
        #timmy_the_turtle.towards(0,0)
ninja_turtle = The_turtle()

#challenge 1
'''
for x in range(1, 5):
    ninja_turtle.creating_square()
'''

#challenge 2
'''
for _ in range(15):
    ninja_turtle.drawing_dashes()
'''
#challenge 3
'''
for shape_side in range(3, 11):
    ninja_turtle.drawing_shapes(shape_side)
'''

#challenge 4
'''
x = True
while x:

    random_num = randint(0, 1)
    ninja_turtle.changing_line_color()
    if random_num == 1:
        ninja_turtle.walk()
        ninja_turtle.right_direction()
    else:
        ninja_turtle.walk()
        ninja_turtle.left_direction()
'''

#challenge 5
'''
ninja_turtle.drawing_circle(5)
'''
for y in range(-150,350,50):
    ninja_turtle.turtle_position(y)
    for x in range(9):
        ninja_turtle.drawing_dot()
        ninja_turtle.turtle_forward()
        ninja_turtle.drawing_dot()




screen = Screen()
screen.exitonclick()
