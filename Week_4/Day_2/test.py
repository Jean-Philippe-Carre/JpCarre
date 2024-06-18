

names_list = ["Alice", "Bob", "Charlie"]
print(names_list,'\n')

def add_string_to_names(names, add_string):
    modified_names = [name + add_string for name in names]
    return modified_names

added_string = " Smith"
names_list = add_string_to_names(names_list, added_string)
print('\n', names_list,'\n')
