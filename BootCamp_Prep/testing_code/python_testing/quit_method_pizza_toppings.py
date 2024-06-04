topping_list = []
while True:
    user_input = input('Enter topping, when you are done, enter \'quit\': ')
    if user_input == 'quit':
        break
    else:
        print(f'{user_input} will be added to your pizza')
        topping_list.append(user_input)
        toppings_price = 2.5 * len(topping_list)
        total_price = 10 + toppings_price

print(f'{topping_list} will be added to your pizza.\n Total price for pizza and toppings: usd {total_price}')
