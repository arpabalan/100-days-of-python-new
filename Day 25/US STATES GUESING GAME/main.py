import turtle
from pprint import pprint
from turtle import Screen, Turtle
import pandas
from Scoreboard import Scoreboard

#scoreboard = Scoreboard()
screen = Screen()
screen.title("U.S. STATES GAME.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

estate_list = []
data = pandas.read_csv("50_states.csv")
missing_state = []
guest_state = []

for estate in data["state"]:
    estate_list.append(estate)
print(estate_list)
counter = 50
score = 0
is_on = True
while is_on:
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?")
    state = data[data["state"]==answer_state.capitalize()]
    counter -= 1
    if answer_state.capitalize() in estate_list:
        guest_state.append(answer_state.capitalize())
        timmy = Turtle()
        timmy.penup()
        timmy.color("black")
        timmy.goto(int(state["x"]),int(state["y"]))
        timmy.hideturtle()
        timmy.write(answer_state.capitalize())
        score += 1
    elif answer_state == "exit":
        for x in estate_list:
            if x not in guest_state:
                missing_state.append(x)
        is_on = False
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")

    if counter == 0:
        is_on = False


screen.exitonclick()

