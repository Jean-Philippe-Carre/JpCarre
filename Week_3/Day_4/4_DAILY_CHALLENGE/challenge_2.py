
user_input = input(
    '\n Enter any word, but duplicate some letters in the word,ie \'ppoeem\': ')

list = list(dict.fromkeys(user_input))
# print('\n',list)

new_word = ''.join(list)
print('\n You meant '+'\''+new_word+'\''+',right...\n')
