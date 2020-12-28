'''
#Lambda is an anonymous function means that a function is without a name
#Syntax: lambda arguments: expression
#This function can have any number of arguments but only one expression, which is evaluated and returned.
#One is free to use lambda functions wherever function objects are required.
'''


cube = lambda y: y * y * y
print(cube)
print(cube(5))

adder = lambda x, y: x + y
print (adder (1, 2))

'''IIFE stands for immediately invoked function execution.
It means that a lambda function is callable as soon as it is defined
'''
adder = (lambda x, y: x + y)(1, 4)
print(adder)
