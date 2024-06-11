
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores':  7000,
    'major_color': {'France': 'blue',
                    'Spain': 'red',
                    'US': 'pink,green'}
}

# 3. Changing the number of stores to 2

brand['number_stores'] = '2'
print('\n Number of stores now:', brand['number_stores'])

# 4. Printing sentence explaining who Zara clients are

print('\n Types of Zara clients are: ', *(brand['type_of_clothes']), sep=",")
print('\n')

# 5. Adding a new key called country_creation with a value of Spain

brand['country_creation'] = 'Spain'
for key, value in brand.items():
    print('', key.capitalize(), ':', value)

# 6. Check if key international_competitors is in dictionary, and Add store Desigual to international competitors

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

print('\n International Competitors:', *
      brand['international_competitors'], sep=", ")

# 7. Delete the information about the date of creation
print('\n')
del brand['creation_date']
for key, value in brand.items():
    print('', key.capitalize(), ':', value)

# 8. Print the last international competitor

print('\n Last international competitor in list:',
      brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US

print('\n Major clothes colors in the US: ', brand['major_color']['US'])

# 10. Print the length of the dictionary ( no of key-value pairs )

print('\n No of Key-Value pairs:', len(brand))

# 11. Print the keys of the dictionary

print('\n', brand.keys())

# 12. Create another dictionary

more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

# 13. Add the information from more_on_zara to brand

print('\n')
brand.update(more_on_zara)
for key, value in brand.items():
    print('', key.capitalize(), ':', value)

print('\n', brand['number_stores'], '\n')
