
list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1] 

[list1.extend(l) for l in (list2,list3,list4)]

# Instruction 2a
print('\n','. List of numbers, in a single line: \n\n',list1)

# Instruction 2b
list1.sort(reverse = True)
print('\n','. List of numbers, in descending order: \n\n',list1)

# Instruction 2c
print('\n', '. Sum of all the numbers:',sum(list1))

# Instruction 3
print('\n . First & last value in the list:',list1[::len(list1)-1])

# Instruction 4
a_list = sorted(i for i in list1 if i > 50)
print('\n . Values greater than 50 in the list:\n\n', a_list)

# Instruction 5 
b_list = sorted(i for i in list1 if i < 10)
print('\n . Values smaller than 10 in the list:\n\n', b_list)

# Instruction 6
square = [i**2 for i in list1]
print('\n . Square all the values in the list:\n\n',square)

# Instruction 7
list1 = list(dict.fromkeys(list1))
print('\n . List with all duplicates removed:\n\n',list1)
print('\n . Number of elements in new list:',len(list1))

# Instruction 8
average = sum(list1) / len(list1)
print('\n . Average of all the numbers:',average)

# Instruction 9
print('\n . Largest number in list:',max(list1))

# Instruction 10
print('\n . Smallest number in list:',min(list1))







