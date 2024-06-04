secret_word = 'code'

while True:
  user_input = input('Guess the secret word: ')
  if user_input == secret_word:
    print('Congrats! You win!')
    break
  else:
    print('Wrong guess...')