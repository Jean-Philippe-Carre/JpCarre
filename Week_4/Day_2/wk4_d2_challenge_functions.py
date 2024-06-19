#
# Given a “Matrix” string:

#     7ii
#     Tsx
#     h % ?
#     i
#     sM
#     $a
#     # t%
#     ^r!

# The matrix is a grid of strings(alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:

# 7	i i
# T	s x
# h % ?
# i	  #
# s	M
# $	a
# # t %
# ^	r !

# Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
# To reproduce the grid, the matrix should be a 2D list, not a string


# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if / else statements to check the data
# ● String for the output of the secret message

# Hint(if needed): Look at the remote learning “Matrix” videos


from itertools import islice


def convert(lst, var_lst):
    idx = 0
    for var_len in var_lst:
        yield lst[idx: idx + var_len]
        idx += var_len


string = '7ii-Tsx-h%?-i #-sM -$a -#t%-^r!'
lst = list(string.split("-"))
var_lst = [1, 1, 1, 1, 1, 1, 1, 1]
print('\n This is the string converted into a 2d list:\n')
print(list(convert(lst, var_lst)), '\n')

print("-----------\n")
print('This is the 2d list in grid form:\n')
for i in lst:
    print(i)
print("\n-----------")


def crack_matrix(lst):
    cleaned_strings = []
    num_rows = len(lst)
    num_cols = len(lst[0]) if lst else 0

    for col in range(num_cols):
        column_alphabets = []
        for row in range(num_rows):
            # Check if element is a string and contains alphabetic characters
            if isinstance(lst[row][col], str):
                cleaned_value = ''.join(
                    char if char.isalpha() else ' ' for char in lst[row][col])
                column_alphabets.append(cleaned_value)

        # Join column alphabets with space and append to cleaned_strings
        cleaned_strings.append(' '.join(column_alphabets))

    # Join all cleaned strings to form the final result
    final_string = ''.join(cleaned_strings)

    return final_string


result = crack_matrix(lst)
print("\n This is the decrypted message:")
print('\n', result)
print("\n")
