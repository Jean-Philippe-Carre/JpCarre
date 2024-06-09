
from collections import Counter

string = '''New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'''

list = string.split()
# print('\n',list)
print('\n',string)
print('\n')

freq = Counter(list).most_common()
for elem in freq:
    print(*elem, sep=':')

