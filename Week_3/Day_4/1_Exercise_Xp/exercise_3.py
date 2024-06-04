basket = ['banana', 'apples', 'oranges', 'blueberries']
print(basket)

basket.pop(0)
basket.pop(2)

print(basket)

basket.append('kiwi')
basket.insert(0,'apples')

print(basket)

print('There are ', basket.count('apples'), 'items named \'apples\' in basket')

basket.clear()

print(basket)