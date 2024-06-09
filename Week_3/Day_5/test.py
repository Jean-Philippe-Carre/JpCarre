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

sample_dict = {
    "class": {"student": {"name": "Mike",
                          "marks": {"physics": 70,
                                    "history": 80
                                    }
                          }
              }
}
print('\n', sample_dict["class"]["student"]["marks"]["history"])
print('\n')

# my_dog = {"name":"rufus", "age":4}
# my_dog["name"] = "rex"
# print(my_dog["name"])k


shirts = {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
}

print('\n', shirts.keys(), '\n')
