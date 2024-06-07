
win_count = 0
lose_count = 0

while True:
    user_input = input('\n Try to guess the number that the computer will generate, from 1 to 9: ')

    import random
    random_number = random.randint(1,9)
    print('\n Computer-generated random number: ',random_number,'\n')

    if random_number == int(user_input):
        win_count += 1
        print(' Congrats!! You win!!')
        print(f'  Total games won: {win_count}')
        print(f'  Total games lost: {lose_count}','\n')
        break

    elif random_number != int(user_input):
        lose_count += 1
        try_again = input(' Better luck next time...Try again? y/n: ')    
        if try_again == 'n':
            print('\n Game Over','\n')
            print(f' Total games won: {win_count}')
            print(f' Total games lost: {lose_count}','\n')
            break

   
         
