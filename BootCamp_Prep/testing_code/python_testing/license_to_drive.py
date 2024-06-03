age = input('Age: ')
is_licensed = input('Licensed? - yes or no: ')
is_old = int(age) > 21

# is_old = True
# is_licensed = True

if is_old and is_licensed:
    print('You are old enough to drive and have a license.')
elif is_old and not(is_licensed):
    print('You are old enough to drive but you are not licensed.')
else:
    print('You are not old enough to have a license and drive.')


