paragraph = '''Find an interesting paragraph of text online. Please keep it appropriate to the social context of our class. Paste it to your code, and store it in a variable. Let’s analyze the paragraph. Print out a nicely formatted message saying: How many characters it contains, this one is easy. How many sentences it contains. How many words it contains. How many unique words it contains.'''

print('\n',paragraph)
print('\n Number of characters in paragraph:',len(paragraph))

# Number of sentences
from collections import Counter 
ending = ('.')
c = Counter(paragraph) 
v = 0 
for p in ending: 
	if p in c: 
		v += c[p] 
print(f"\n Number of sentences in paragraph: {v}") 

# Number of words
words = paragraph.split()
count = len(words)
print('\n Number of words in paragraph:',count,'\n')
	
# Number of unique words
# from collections import Counter
# counter = Counter(paragraph)
# unique = [item for item, count in counter.items() if count == 1]
# if unique:
#     print("Number of unique words:", unique)


