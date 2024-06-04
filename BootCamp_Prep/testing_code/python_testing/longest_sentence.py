# while password != 'secret':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')


user_input = input('Enter a sentence without the letter A in it: ')
user_input2 = input('Enter a longer sentence without the letter A in it: ')

length1 = len(user_input)
length2 = len(user_input2)

while length2 > length1:
    print(user_input2)
print('You lose')