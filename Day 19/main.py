from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")

def move_forward():
    timmy_the_turtle.forward(10)

def move_backward():
    timmy_the_turtle.backward(10)

def rotate_counter_clock_wise():
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 5)

def rotate_clock_wise():
    timmy_the_turtle.setheading(timmy_the_turtle.heading() - 5)

def clear_screen():
    timmy_the_turtle.penup()
    timmy_the_turtle.clear()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()


screen.listen()
print(screen.onkey(key="w", fun=move_forward))
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clock_wise)
screen.onkey(key="d", fun=rotate_clock_wise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()