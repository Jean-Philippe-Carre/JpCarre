# Write a function called find_max, which should take a list and return the largest number in that list
# put this function in the utils module
# import the utils module in the main module and call find_max()
# get the result and print it on the terminal


from utils import find_max
import random

# user_input = input(
#     "Enter a list of 5 numbers from 1 to 50, seperated by comas: ")
# numbers = [int(number) for number in user_input.split(",")]

numbers = []
for i in range(5):
    numbers.append(random.randint(1, 10))

print(numbers)

print(f"The largest number in this list is: {find_max(numbers)}")
