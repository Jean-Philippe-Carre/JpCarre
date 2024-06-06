num = input('Enter a number between 1 & 100: ')
num =int(num)

if num%3 == 0:
    print('Fizz')
elif num%5 == 0:
    print('Buzz')
elif num%3 == 0 and num%5 == 0:
    print('FizzBuzz')

else:
    print(f'{num} is neither a multiple of 3 nor a multiple of 5')
	

