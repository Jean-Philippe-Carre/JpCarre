string = input('Enter a short string: ')
length = len(string)

if length < 10:
    print('String not long enough') 
elif length > 10:
    print('String too long')
elif length == 10:
    print('Perfect string!!')
    print('First and last letter of the string are: ' ,string[0],string[-1])

    for letter in string:
        print(letter)
       
        
    
    
    
   