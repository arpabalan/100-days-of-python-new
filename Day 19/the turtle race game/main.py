from copyreg import pickle
from random import randint
from turtle import Turtle, Screen
import random



michael_angelo = Turtle()
donatelo = Turtle()
leonardo = Turtle()
rafael = Turtle()
screen = Screen()
ninja_turtles = [michael_angelo, donatelo, leonardo, rafael]
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Fastest Ninja Turtle", prompt="Who is the fastest ninja turtle [michael angelo, leonardo, rafael, donatelo]?: ")

michael_angelo.shape("turtle")
michael_angelo.color("blue")
michael_angelo.penup()
michael_angelo.goto(x=-230,y=0)


donatelo.shape("turtle")
donatelo.color("orange")
donatelo.penup()
donatelo.goto(x=-230,y=-50)

rafael.shape("turtle")
rafael.color("red")
rafael.penup()
rafael.goto(x=-230,y=50)

leonardo.shape("turtle")
leonardo.color("purple")
leonardo.penup()
leonardo.goto(x=-230,y=100)



is_on = False
if user_bet:
    is_on = True

while is_on:


    for ninja_turtle in ninja_turtles:
        random_distance = randint(0, 10)
        ninja_turtle.forward(random_distance)
        if ninja_turtle.xcor() > 230:
            ninja_turtle_winner = ninja_turtle.pencolor()
            if ninja_turtle_winner == "blue":
                print("The fastest ninja turtle is Michael Angelo!")
            elif ninja_turtle_winner == "orange":
                print("The fastest ninja turtle is Donatelo!!")
            elif ninja_turtle_winner == "purple":
                print("The fastest ninja turtle is Rafael!!")
            else:
                print("The fastest ninja turtle is Leonardo!!")
            is_on = False








screen.exitonclick()