import random
from art import logo


print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_card = []
computer_card = []


def random_card():
    for x in range(0, 2):
        my_card.append(random.choice(cards))
        computer_card.append(random.choice(cards))


random_card()


def my_card_sum():
    my_card_sum = sum(my_card)
    if 11 in my_card and my_card_sum > 21:
        my_card.remove(11)
        my_card.append(1)
        my_card_sum = sum(my_card)
        return my_card_sum
    else:
        return my_card_sum


def computer_card_sum(computer_card_sum):
    if 11 in computer_card and computer_card_sum > 21:
        computer_card.remove(11)
        computer_card.append(1)
        computer_card_sum = sum(computer_card)
        return computer_card_sum
    else:
        return computer_card_sum


computer_card_summ = 0
computer_card_summ += sum(computer_card)
computer_hand = True
while computer_hand == True:
    if computer_card_summ < 17:
        computer_card.append(random.choice(cards))
        computer_card_summ = sum(computer_card)
    else:
        x = computer_card_sum(computer_card_summ)
        computer_hand = False


def identifying_winner(computer_card_sum, my_card_sum):
    if my_card_sum == 21 and computer_card_sum != 21:
        print(f"Your card {my_card}total: {my_card_sum}")
        print(f"Computer card {computer_card}total: {computer_card_sum}")
        print("You Win")
        print("Youve Won a Black Jack")
    elif computer_card_sum == 21 and my_card_sum != 21:
        print(f"Your card {my_card} total: {my_card_sum}")
        print(f"Computer card {computer_card} total: {computer_card_sum}")
        print("You Lose")
    elif computer_card_sum > 21 and my_card_sum <= 21:
        print(f"Your card {my_card}total: {my_card_sum}")
        print(f"Computer card {computer_card}total: {computer_card_sum}")
        print("You Win")
    elif my_card_sum > 21:
        print(f"Your card {my_card} total: {my_card_sum}")
        print(f"Computer card {computer_card} total: {computer_card_sum}")
        print("You went over. You Lose!!")

    elif computer_card_sum > my_card_sum:
        print(f"Your card {my_card} total: {my_card_sum}")
        print(f"Computer card {computer_card} total: {computer_card_sum}")
        print("You Lose")
    elif computer_card_sum < my_card_sum:
        print(f"Your card {my_card}total: {my_card_sum}")
        print(f"Computer card {computer_card}total: {computer_card_sum}")
        print("You Win")
    else:
        print(f"Your card {my_card}")
        print(f"Computer card {computer_card}")
        print("Draw")


hand_another = True
while hand_another == True:
    my_card_summ = my_card_sum()
    print(f"Your card {my_card}total: {my_card_summ}")
    print(f"Computer card {computer_card[0]}")
    hand_another_card = input("Do you want another card? Y or N: ").lower()
    if hand_another_card == 'y':
        my_card.append(random.choice(cards))
        n_card_sum = sum(my_card)
        if n_card_sum > 21:
            my_card_summ = my_card_sum()
            identifying_winner(computer_card_sum=x, my_card_sum=my_card_summ)
            hand_another = False

    elif hand_another_card == 'n':
        identifying_winner(computer_card_sum=x, my_card_sum=my_card_summ)
        hand_another = False