"""with open("weather_data.csv", "r") as file:
    data = []
    for x in file.readlines():
        data.append(x.strip())
    print(data)
"""
import pandas as pd

"""
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
    temperatures.remove('temp')
    print(temperatures)"""

import pandas
"""data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()
temperature_avg = sum(temperatures)/len(temperatures)
#print(temperature_avg.__round__(2))
max_temp = data["temp"].max()
print(data)
list_of_days = data["day"].to_list()
print(list_of_days[temperatures.index(max_temp)])

print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
celcius_to_farenheit = (monday.temp*9)/5  + 32
print(celcius_to_farenheit)

"""
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250826.csv")
print(data["Primary Fur Color"])

color_black = 0
color_gray = 0
color_cinnamon = 0
color_count_list = []
for color in data["Primary Fur Color"]:
    if color == "Gray":
        color_gray += 1
    elif color == "Black":
        color_black += 1
    else:
        color_cinnamon +=1

color_count_list.append(["Gray", color_gray])
color_count_list.append(["Black", color_black])
color_count_list.append(["Cinnamon", color_cinnamon])

df_from_list = pd.DataFrame(color_count_list, columns=["Primary Fur Color","Count"])
df_from_list.to_csv("Squirrel_count.csv")


































