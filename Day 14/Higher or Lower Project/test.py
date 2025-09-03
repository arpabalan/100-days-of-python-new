import random

list_data = [100, 200, 300, 400, 500, 99, 87]
random_object_a = []
counter = 1
points = 0

for x in range(1, 3):
    random_number = random.randrange(0, len(list_data))
    random_object_a.append(list_data[random_number])

while counter != 0:
    if random_object_a[0] == random_object_a[1]:
        # print("same")
        list_data.pop(list_data.index(random_object_a[1]))
        random_number = random.randrange(0, len(list_data))
        random_object_a.pop(1)
        random_object_a.append(list_data[random_number])

    else:
        compare_object = input("Compare who is higher a or b: ")
        if compare_object.lower() == 'a':
            if random_object_a[0] > random_object_a[1]:
                print("object 1 is higher")
                random_object_a.pop(1)
                points += 1
            else:
                print("you lost!!")
                print(points)
                break

        elif compare_object.lower() == 'b':
            if random_object_a[1] > random_object_a[0]:
                print("object 2 is higher")
                random_object_a.pop(0)
                points += 1
            else:
                print("You lost!!!")
                print(points)
                break
        else:
            print("invlid Input!")
            random_object_a.pop(1)

        random_number = random.randrange(0, len(list_data))
        random_object_a.append(list_data[random_number])
        # print(random_object_a)