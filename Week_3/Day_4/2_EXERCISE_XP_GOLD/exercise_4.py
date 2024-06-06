num1 = input('\nEnter first number: ')
num2 = input('Enter second number: ')
num3 = input('Enter third numbers: ')

if num1 > num2 and num1 > num3:
    print(f'\nThe greatest number is: {num1} \n')
elif num2 > num1 and num2 > num3:
    print(f'\nThe greatest number is: {num2} \n')
elif num3 > num1 and num3 > num2:
    print(f'\nThe greatest number is: {num3} \n')

        