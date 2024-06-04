user_input = input('Enter your favourite fruits, leave a space between the answers, no comas: ')

fav_fruits = user_input.split()

print(fav_fruits)

user_input2 = input('Enter any fruit: ')
if user_input2 in fav_fruits:
    print('You chose one of your favourite fruits, enjoy!!')
else:
    print('You chose a new fruit, i hope you enjoy...')

