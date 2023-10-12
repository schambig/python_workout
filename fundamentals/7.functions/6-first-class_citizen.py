'''
The term "first-class citizen" in programming languages, including Python,
refers to the concept that functions (or other entities like variables or objects)
can be treated like any other value.
Specifically, in a language where functions are first-class citizens, functions can be:
    Assigned to variables.
    Passed as arguments to other functions.
    Returned from other functions.
    Storing in data structures.
'''

# Assigned to variables:
# You can assign a function to a variable, making the variable reference the function.
# This allows you to use the variable to call the function.
def greet(name):
    return f"Hello, {name}!"

my_function = greet
result = my_function("Salo")
print(result)  # Hello, Salo!


# Passed as arguments to other functions:
# You can pass a function as an argument to another function.
def apply(func, arg):
    return func(arg)


def square(x):
    return x * x

result = apply(square, 4)
print(result)  # 16


# Returned from other functions:
# A function can return another function.
def get_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_2 = get_multiplier(2)
result = multiply_by_2(5)
print(result)  # 10

# Storing in data structures:
# Functions can be stored in data structures like lists, dictionaries, and sets.
# This allows you to manage functions in a flexible and organized way.

'''Storing Functions in a List:'''
def square(x):
    return x * x


def cube(x):
    return x * x * x

# Storing functions in a list
function_list = [square, cube]

# Accessing and calling functions from the list
result1 = function_list[0](5)
result2 = function_list[1](3)

print(result1)  # 25 (square of 5)
print(result2)  # 27 (cube of 3)


'''Storing Functions in a Dictionary:'''
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

# Storing functions in a dictionary
function_dict = {
    'add': add,
    'subtract': subtract
}

# Accessing and calling functions from the dictionary
result_add = function_dict['add'](10, 5)
result_subtract = function_dict['subtract'](8, 3)

print(result_add)       # 15 (10 + 5)
print(result_subtract)  # 5 (8 - 3)


'''
Storing Functions in a Set:
In this example, multiply_by_2 and square functions are stored in a set,
and then a generator expression is used to find and execute the desired function
based on its name.
'''
def multiply_by_2(x):
    return x * 2


def square(x):
    return x * x

# Storing functions in a set
function_set = {multiply_by_2, square}

# Accessing and calling functions from the set, using a generator expression
result1 = next(func for func in function_set if func.__name__ == 'multiply_by_2')(3)
result2 = next(func for func in function_set if func.__name__ == 'square')(4)

print(result1)  # Output: 6 (3 * 2)
print(result2)  # Output: 16 (4 * 4)

'''
While the example above demonstrates one way to call functions from a set using
a generator expression, we can use a more straightforward approach by directly
calling each function in a loop or through other iteration methods.
Here's an example:
'''
def multiply_by_2(x):
    return x * 2


def square(x):
    return x * x

# Storing functions in a set
function_set = {multiply_by_2, square}

# Calling functions from the set
# This loop iterates through each function in the function_set and
# calls it with the input_value.
# This approach is more explicit and easier to read than the generator expression
# if you want to call all functions in the set.
input_value = 3
for func in function_set:
    result = func(input_value)
    print(result)
#  This results in the output:
6  # Output of multiply_by_2(3)
9  # Output of square(3)
