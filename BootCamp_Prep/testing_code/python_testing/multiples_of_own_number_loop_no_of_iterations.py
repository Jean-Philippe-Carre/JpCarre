
user_input1 = int(input('\n Enter a number: '))
user_input2 = int(input('\n Enter no of iterations: '))

count = 0
list = []

for n in range(1,user_input2+1):
    count += 1
    multiples = user_input1*count
    list.append(multiples)
print('\n Multiples of',user_input1,':',list,'\n')



