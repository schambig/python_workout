'''
In Python, the terms "parameter" and "argument" are often used interchangeably,
but they have slightly different meanings.
    Parameter: A parameter is a placeholder variable defined in the function's declaration.
                It represents the data that will be passed into the function when it is called.
    Argument: An argument is the actual value that is passed to the function when it is called.
                It replaces the placeholder variable (parameter) with a specific value.
In other words, parameters are like blueprints or templates for the data that the function will receive,
while arguments are the actual data that are provided to the function during its execution.
'''

def sum(n1, n2):
    return  n1 + n2, 'Also return this string' # The function return two values

first_num = int(input('Enter the first integer number: ')) # cast to int
second_num = int(input('Enter the second integer number: ')) # cast to int

result, _ = sum(first_num, second_num) # avoid the second value (string) using '_'

print('The result is:', result)
