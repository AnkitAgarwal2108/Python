'''
The filter function is used to select some particular elements from a sequence of elements.
The sequence can be any iterator like lists, sets, tuples, etc.
The elements which will be selected is based on some pre-defined constraint. It takes 2 parameters:
A function that defines the filtering constraint
A sequence (any iterator like lists, tuples, etc.)
filter(function, iterable)
'''

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter(lambda x: x > 4, sequences)
print(filtered_result)
print(list(filtered_result))

randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)
print(list(filteredList))

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)


