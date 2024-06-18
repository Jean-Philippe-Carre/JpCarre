# (1) Using the input function, ask the user for a string. The string must be 10 characters long.
# . If it’s less than 10 characters, print a message which states “string not long enough”.
# . If it’s more than 10 characters, print a message which states “string too long”.
# . If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# (2) Then, print the first and last characters of the given text.

# (3) Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld

# (4) Bonus: Swap some characters around then print the newly jumbled string(hint: look into the shuffle method). For example:
# Hlrolelwod


string = input('\nEnter a short string: ')
length = len(string)

if length < 10:
    print('String not long enough')
elif length > 10:
    print('String too long')
elif length == 10:
    print('Perfect string!!\n')
    print('First and last letter of the string are: ',
          string[0], ',', string[-1], '\n')

    for i in range(1, len(string) + 1):
        substring = string[:i]
        print(substring)

    print("\n")

    import random
    swap = ''.join(random.sample(string, len(string)))
    print(swap)

    print("\n")
    