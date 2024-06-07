alphabet_letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

for letter in alphabet_letters:
    if letter in vowels:
        print(letter, ': vowel')
    else:
        print(letter, ': consonant')

