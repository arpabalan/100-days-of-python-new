import random


numbers = [1,2,3]
"""new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)
"""

################### converting above to list comprehension
"""
new_list = [new_item for item in list]
"""

new_list = [n+1 for n in numbers]
print(new_list)


name = "RJ Pabalan"
new_list = [letter for letter in name]
print(new_list)

new_list = [x*2 for x in range(1,5)]
print(new_list)

################### conditional list comprehension
"""
new_list = [new_item for item in list if test]
"""


############# dictionary comprehension################
# new_dictionary = {item:value for item in list}
# new_dictionary = {key:value for (key,value) in dictionary.items()}
# new_dictionary = {key:value for (key,value) in dictionary.items() if test}

names = ["Alex", "Beth", "Dave","Caroline", "Eleanor","Freddie"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)
students = {student:random.randint(1,100) for student in names}
print(students)
pass_students = {student:score for (student,score) in students.items() if score >= 60}
print(pass_students)