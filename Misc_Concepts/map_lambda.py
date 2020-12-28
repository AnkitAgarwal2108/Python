'''
the map function is used to apply a particular operation to every element in a sequence.
Like filter(), it also takes 2 parameters:
A function that defines the op to perform on the elements
One or more sequences
map(function, iterable, ...)
'''

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map(lambda x: x*x, sequences)
print(list(filtered_result))

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

num1 = [4, 5, 6, 8]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))


def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)





