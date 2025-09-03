from logging import fatal

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


checker = True
def resource_checker(coffee):
    counter = 0
    ingredients = []
    for i in MENU[coffee]["ingredients"].items():
        ingredients.append(i[0])
    for ingredient in ingredients:
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]:
            print(f"print not enough {ingredient}")
            return False
        else:
            return True

def process_coin():
    quarters = float(input("Enter number of quarters: ")) * 0.25
    dimes = float(input("Enter number of dimes: ")) * 0.10
    nickles = float(input("Enter number of nickle: ")) * 0.05
    pennies = float(input("Enter number pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def check_transaction(coffee, user_money):
    if MENU[coffee]['cost'] > user_money:
        print("Not enough money, money refunded....")

    else:
        resources["money"] += MENU[coffee]['cost']
        change = user_money - MENU[coffee]['cost']
        print(f"Here is your change {round(change,2)}$")
        print(f"Here is your {coffee} enjoy!")
        ingredients = []
        for i in MENU[coffee]["ingredients"].items():
            ingredients.append(i[0])
        for ingredient in ingredients:
            resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
        return change



#TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
is_on = True

while is_on:
    coffee = input("What would you like? (espresso/latte/cappuccino):")

#TODO   Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee.lower() == "off":
        print(".....COFFEE Machine powering off...............:)")
        is_on = False

# TODO Print report.
    elif coffee.lower() == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : {resources['money']}$")
    else:
# TODO Check resources sufficient?
        if resource_checker(coffee):
    # TODO Process coins.
            user_coin = process_coin()
            check_transaction(coffee, user_coin)





