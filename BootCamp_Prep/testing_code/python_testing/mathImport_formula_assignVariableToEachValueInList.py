
# Use 100,150,180 as User Input to get 18,22,24 as per exercise instructions 

from math import*

C = 50
H = 30

user_input = input('\n Enter a string of numbers, seperated by comas: ')
list = user_input.split(',')

# formula = int(sqrt((2*C*D)/H))

for num in list:
    D = int(num)
    print('\n   Square root of (2*C*D)/H:', int(sqrt((2*C*D)/H)),'\n')

