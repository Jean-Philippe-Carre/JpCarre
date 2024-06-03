height = input('Enter your height in centimetres please: ')
height = int(height)
limit = 145

if height > limit:
    print('Yes, you are tall enough to ride.')
else:
    print('Nope, you need to grow some more to ride.')