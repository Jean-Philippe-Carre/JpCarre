sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'avocado sandwich',
                   'pastrami sandwich', 'egg sandwich', 'chicken sandwich', 'pastrami sandwich']

print('\n\n Sandwich Orders:\n ', *sandwich_orders, sep=", ")

while True:
    out_of_sandwich = input(
        '\n\t Any sandwiches unavailable? ( Enter \'no\' when done ): ')
    if out_of_sandwich == 'no':
        break

    while True:
        if out_of_sandwich in sandwich_orders:
            sandwich_orders.remove(out_of_sandwich)
        else:
            break

print('\n Sandwich Orders:\n ', *sandwich_orders, sep=", ")

finished_sandwiches = []
prepared_sandwiches = []

while True:
    prepared_sandwiches = input(
        '\n Enter sandwich which is already prepared ( When all sandwiches are prepared, enter \'done\'): ')
    if prepared_sandwiches == 'done':
        break

    else:
        sandwich_orders.remove(prepared_sandwiches)
        finished_sandwiches.append(prepared_sandwiches)
        print('\n\t Remaining sandwiches to be prepared: ',
              *sandwich_orders, sep=", ")

print('\n I made your:\n\t', *finished_sandwiches, sep='\n')
print('\n')
