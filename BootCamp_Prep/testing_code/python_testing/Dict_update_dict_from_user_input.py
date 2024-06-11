
# Part 1: Using an already populated dictionary

# family = {"Rick": 43, 'Beth': 13, 'Morty': 5, 'Summer': 8, 'Faith': 2}

# children_price = 0
# adult_price = 0

# for key, value in family.items():
#     if value < 3:
#         print(key, 'Free')
#     elif 3 < value < 12:
#         children_price += 10
#         print(key, '$10')
#     else:
#         adult_price += 15
#         print(key, '$15')

# total_price = children_price + adult_price

# print('\n')
# print('Total price: $',total_price, '\n')

# *********************************************************
# *********************************************************

# Part 2: Populating the dictionary from user input

family = {}

while True:
    name = input('\n Enter your name: ')
    age = int(input(' Enter your age: '))
    next = input(' Continue? y/n: ')
    family[name] = age

    if next == 'n':
        break

children_price = 0
adult_price = 0

print('\n')
for key, value in family.items():
    if value < 3:
        print('\n', key.capitalize(), 'Free')
    elif 3 < value < 12:
        children_price += 10
        print('\n', key.capitalize(), '$10')
    else:
        adult_price += 15
        print('\n', key.capitalize(), '$15')

total_price = children_price + adult_price

print('\n')
print(' Total price: $', total_price, '\n')
