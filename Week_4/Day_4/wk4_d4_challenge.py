
# Write a function to compute 5/0 and use try / except to catch the exceptions.
# Bonus: use some Buit-in exceptions of Python: Look here

def compute():
    try:
        user_input = int(input('\nEnter a number: '))
        result = user_input / 0
        print(result)

    except ZeroDivisionError:
        print("Zero Division Error: divided by zero not possible\n")


compute()
