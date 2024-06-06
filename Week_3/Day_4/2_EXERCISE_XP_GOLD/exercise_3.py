names = ['Samus','Cortana','V','Link','Mario','Cortana','Samus']

while True:
    user_input = input('\nEnter your name: ')
    if user_input.capitalize() in names:
        print('\nIndex in list: ', names.index(user_input.capitalize()),'\n')
        break
    else:
        print('\n\tYour name is not in the list')

