'''
The reduce function, like map(), is used to apply an operation to every element in a sequence but
the reduce() function to compute an output.
'''

from functools import reduce
sequences = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, sequences)
print(product)

def calculateSquare(m,n):
    return m*n

numbers = (1, 2, 3, 4)
result = reduce(calculateSquare, numbers)
print(result)

