# user_input = input('Write a sentence without the letter A in it: ')
# count = len(user_input)
# user_input2 = input('Now, write a sentence longer than the previous one, still without A in it: ')



# if len(user_input2) > count:
#     print('Congrats! This sentence is longer than the previous one. Try again.')

# else:
#     print('you fail.')


user_input = input('Write a sentence without the letter A in it: ')
count = len(user_input)

while len(user_input) > count:
    print('Now, write a longer sentence without the letter A in it: ')
    

