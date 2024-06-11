# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez',
#     'age': 45
#     }

# print('\n Your last name is',rick_dict['last_name'])
# print(' and you are',rick_dict['age'],'years old\n')

# a_dict = {'color': 'blue',
#           'fruit': 'apple',
#           'pet': 'dog'}
# print('\n',a_dict.items())``

# for key, value in a_dict.items():
#     print(key,'o-->',value)

# sample_dict = {
#     "class": {"student": {"name": "Mike",
#                           "marks": {"physics": 70,
#                                     "history": 80
#                                     }
#                           }
#               }
# }
# print('\n', sample_dict["class"]["student"]["marks"]["history"])
# print('\n')

# my_dog = {"name":"rufus", "age":4}
# my_dog["name"] = "rex"
# print(my_dog["name"])k


# shirts = {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
# }

# print('\n', shirts.values(), '\n')

# rick_dict = {
#     'first_name': 'Rick',
#     'last_name': 'Sanchez'
# }
# print(rick_dict.items())

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# z = {**x, **y}
# print(z)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# x.update(y)
# print(x)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# del sample_dict['name']
# del sample_dict['salary']
# print(sample_dict)

# my_books = {
#     "title": "Harry Potter",
#     "author": "JK Rowling",
# }

# for x,y in my_books.items():
#     print('\n The',x,'is',y)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}

# for item in enumerate('abcd'):
#     print(item)
# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}

# for item in enumerate('1234'):
#     print(item)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}

# for index_count,letter in enumerate("abcd"):
#     print('\n At index',index_count,'the letter is',letter,'\n')

# list1 = [1, 2, 3]
# list2 = ["a", "b", "c"]
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# for item in zip(list1,list2,list3):
#     print(item,'\n')

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='')
# print('\n')

list1 = [2, 3, 4]
list2 = [100, 200, 300]

my_list = []

for i in list1:
    for j in list2:
        my_list.append(i*j)
print(my_list)
