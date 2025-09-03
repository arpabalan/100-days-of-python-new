import random
import game_data
import art


random_artist = []
points = 0
while_winning = True

def get_random_artist(number=1):
    for i in range(number):
        radom_object = random.randrange(1, len(game_data.data))
        random_artist.append(game_data.data[radom_object])

get_random_artist(2)

while while_winning:
    print(art.logo)
    print(f"Who has more follower {random_artist[0]['name']}")
    print(art.vs)
    print(random_artist[1]['name'])

    user_input = input(f"Enter A for {random_artist[0]['name']} or B for {random_artist[1]['name']}\n")
    if random_artist[0]['follower_count'] == random_artist[1]['follower_count']:
        random_artist.pop(game_data.data.index(random_artist[1]['name']))
        random_artist.pop(random_artist[1])
        get_random_artist()
    else:
        if user_input.upper() == 'A':
            if random_artist[0]['follower_count'] > random_artist[1]['follower_count']:
                print(f"{random_artist[0]['name']} has more follower")
                points += 1
                random_artist.pop(1)
                get_random_artist()
            else:
                print('You lost')
                while_winning = False
                print("Your Score: ",points)

        elif user_input.upper() == 'B':
            if random_artist[1]['follower_count'] > random_artist[0]['follower_count']:
                print(f"{random_artist[0]['name']} has more follower")
                points += 1
                random_artist.pop(0)
                get_random_artist()
            else:
                print('You lost')
                while_winning = False
                print("Your Sore: ",points)
        else:
            print("Invalid Input!")




