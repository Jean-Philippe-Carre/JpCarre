my_fav_numbers = {9, 10, 32}

new_numbers = [15,23]

my_fav_numbers.update(new_numbers)

print(my_fav_numbers)

my_fav_numbers.discard(23)

print(my_fav_numbers)

friend_fav_numbers = {11,18,78,89,99}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)