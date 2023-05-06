with open('./Input/Letters/starting_letter.txt') as file:
    file = file.read()

with open('./Input/Names/invited_names.txt') as names:
    names = names.read()

list_names = names.split('\n')  # список имен

for name in list_names:
    new_letter = file.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_fot_{name}', mode='w') as f:
        f.write(new_letter)
