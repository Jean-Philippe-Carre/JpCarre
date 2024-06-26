from functools import reduce
my_list = [1, 3, 5, 7]
reduced_list = reduce(lambda first, second: first+second, my_list)

print(reduced_list)