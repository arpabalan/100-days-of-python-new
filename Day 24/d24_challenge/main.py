#TODO: Create a letter using starting_letter.txt

letter_list = []
names = []
with open("./Input/Letters/starting_letter.txt") as file:
    sample_letter = file.read()

    with open("./Input/Names/invited_names.txt") as f:
        for name in f.readlines():
            new_letter = sample_letter.replace('[name]',name.strip())
            letter_list.append(new_letter)
            names.append(name.strip())

print(letter_list)
print(names)
for name,letter in zip(names,letter_list):
    with open(f'./Output/ReadyToSend/letter_to_{name}.txt', 'w') as invited:
        invited.write(letter)


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


