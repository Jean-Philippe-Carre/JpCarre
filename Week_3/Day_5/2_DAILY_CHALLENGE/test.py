# Challenge 2:

# (1) Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# (2) Sort the list in alphabetical order.
# (3) Return “Nothing” if you can’t afford anything from the store.
# . Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# The key is the product, the value is the price

# *******************************************************

store_items = {"water(6-pack)": "$10",
               "tv": "$1,000",
               "fertilizer": "$20",
               "water boiler": "$85",
               "honey": "$3",
               "fan": "$14",
               "toaster": "$50",
               "pan": "$100",
               "kitchen grinder": "$75",
               "phone": "$999",
               "speakers": "$300",
               "laptop": "$5,000",
               "pc": "$1,200"
               }

affordable_items = {}
bought_items = []
wallet = 300
total_price = 0

print('These are the items in the store, as well as their price:')
for key, value in store_items.items():
    print('  ', key.capitalize(), value)

while True:
    user_input = input(f'\n You have ${
                       wallet} in your wallet. What would you like to buy? Enter quit when you want to check out: ')

    if user_input == 'quit':
        break
    else:
        bought_items.append(user_input)

    store_items[user_input] = int(
        store_items[user_input].replace("$", "").replace(",", ""))
    if store_items[user_input] > wallet:
        print("\n Not enough money in wallet, choose something else...")
        bought_items.remove(user_input)
    else:
        wallet -= store_items[user_input]
        total_price += store_items[user_input]

print('\n Bought Items:', bought_items, "\n")
print(f"Total cost: ${total_price}\n")
print(f'Remaining money in wallet: ${wallet}\n')
