
family = {"Rick": 43, 'Beth': 13, 'Morty': 5, 'Summer': 8, 'Faith': 2}

for key, value in family.items():
    if value < 3:
        print(key, 'Free')
    elif 3 < value < 12:
        print(key, '$10')
    else:
        print(key, '$15')
print('\n')
