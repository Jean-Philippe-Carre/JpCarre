
baby_ticket = 0
children_ticket = 10
adult_ticket = 15

baby_count = 0
children_count = 0
adult_count = 0

while True:
    age = input('Enter age please, when you have finished, enter \'quit\': ')
    if age == 'quit':
        break
    else:
        if int(age) <= 3:
            baby_count += 1
            print(f'{baby_count} baby: Free')

        elif int(age) > 3 and int(age) <= 12:
            children_count += 1
            total_children_cost = (children_count * 10)
            print(f'{children_count} person(s) between 3 & 12: $ {total_children_cost}')   

        elif int(age) > 12:
            adult_count += 1
            total_adult_cost = (adult_count * 15)
            print(f'{adult_count} adult: $ {total_adult_cost}')

total_cost = ( total_children_cost + total_adult_cost )
print(f'Your booking:\n {baby_count} baby(ies): Free\n {children_count} person(s) between 3 & 12: {total_children_cost}\n {adult_count} adult(s): {total_adult_cost}\n  Total cost: {total_cost}')



