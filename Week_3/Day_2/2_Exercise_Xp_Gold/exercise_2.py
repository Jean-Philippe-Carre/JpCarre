month = input('Enter the numerical value of a month, ie february is 2, april is 4, etc..: ')
month = int(month)

spring = 3,4,5
summer = 6,7,8
autumn = 9,10,11
winter = 12,1,2

if month in spring:
    print('Spring')
elif month in summer:
    print('Summer')
elif month in autumn:
    print('Autumn')
else:
    print('Winter')

