
words = []
user_input = input('\nEnter 7 words please: ')
words = user_input.split()
print('\nThe words you have chosen are:', *words, sep = ', ')

letter = input('\nNow enter a letter: ')
for word in words:
    if letter in word:
        print(' ',letter,'is at index',word.index(letter),'in',word )
    else:
        if letter not in word:
            print(' ',letter,'is not in',word)

print('\n Now you know the position of the letter in each of your words, cool right!')
print('\n')



