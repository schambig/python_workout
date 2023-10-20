'''
A decorator is a special type of function that is used to modify or extend
the behavior of another function or method.
Decorators are commonly used to wrap or enhance the functionality of functions without
modifying their actual code.
They provide a way to separate concerns and make code more modular and reusable.

The syntax for using decorators involves placing the decorator symbol @ followed by
the decorator function name above the function definition.
Here's a simple example:
    @my_decorator
    def my_function():
        # function code here
        pass
'''
'''
a -> Decorator function
b -> Function to decorate
c -> 'Decorated function'

a(b) -> c
'''
def function_a(function_b):

    def function_c():
        print('Before calling function_b')

        function_b()

        print('After calling function_b')

    return function_c

# Using the decorator function
@function_a
def greeting():
    print('Hello from greeting function')

# greeting()
# Output:
# Before calling function_b
# Hello from greeting function
# After calling function_b

# Using the decorator on another function
@function_a
def sum():
    print(10 + 30)

sum()
# Output:
# Before calling function_b
# 40
# After calling function_b
