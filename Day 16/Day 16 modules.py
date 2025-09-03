
"""import turtle





from turtle import Turtle, Screen

import prettytable
prettytable.

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)
print(timmy)
my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
"""
from prettytable import PrettyTable


table = PrettyTable()

table.add_column('Pokimon Name',['Sindaquile','Bayleaf', 'Totodile'])
table.add_column("Type",['Fire','Grass', 'Water'])
table.align = "l"
print(table)