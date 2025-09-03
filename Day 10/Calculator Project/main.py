import art
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/'  :divide
}


continue_calculate = True
first_number = float(input("Input first number here: "))
chosen_operation = input("Enter your desired operation here [+],[-],[*],[/] : ")
second_number = float(input("Input second number here: "))
result = operations[chosen_operation](first_number, second_number)
print(result)
while continue_calculate:
    continue_to_calculate = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
    if continue_to_calculate == 'y':
        continue_calculate = True
        chosen_operation = input("Enter your desired operation here [+],[-],[*],[/] : ")
        new_number = float(input("Enter a new number: "))
        result = operations[chosen_operation](result, new_number)
        print(result)
    elif continue_to_calculate == 'n':
        continue_calculate = True
        print(art.logo)
        print('\n'*20)
        result = 0
        first_number = float(input("Input first number here: "))
        chosen_operation = input("Enter your desired operation here [+],[-],[*],[/] : ")
        second_number = float(input("Input second number here: "))
        result = operations[chosen_operation](first_number, second_number)

    else:
        continue_calculate = False



