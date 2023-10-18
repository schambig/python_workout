'''
In Python, decorators are a powerful way to modify or extend the behavior of functions.
Decorators can also take parameters, such as *args and **kwargs.
Here are a few examples of function decorators that accept such parameters:
'''

# Example 1: Decorator with *args
def args_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments passed to the function:", args)
        result = func(*args, **kwargs)
        return result
    return wrapper

@args_decorator
def example_function(a, b, c):
    print("Inside the function")
    return a + b + c

result = example_function(1, 2, 3)
print("Result:", result)
# Output:
# Arguments passed to the function: (1, 2, 3)
# Inside the function
# Result: 6


# Example 2: Decorator with **kwargs
def kwargs_decorator(func):
    def wrapper(*args, **kwargs):
        print("Keyword arguments passed to the function:", kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@kwargs_decorator
def example_function(x, y, z):
    print("Inside the function")
    return x * y * z

result = example_function(x=2, y=3, z=4)
print("Result:", result)
# Output:
# Keyword arguments passed to the function: {'x': 2, 'y': 3, 'z': 4}
# Inside the function
# Result: 24


# Example 3: Decorator with both *args and **kwargs
def args_kwargs_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments passed to the function:", args)
        print("Keyword arguments passed to the function:", kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@args_kwargs_decorator
def example_function(a, b, c, x, y, z):
    print("Inside the function")
    return a + b + c + x * y * z

result = example_function(1, 2, 3, x=2, y=3, z=4)
print("Result:", result)
# Output:
# Arguments passed to the function: (1, 2, 3)
# Keyword arguments passed to the function: {'x': 2, 'y': 3, 'z': 4}
# Inside the function
# Result: 30


'''
In this example, the `log_function_call` decorator is applied to two functions:
    add_numbers and multiply_numbers.
When these functions are called, the decorator prints information about the function call,
including the arguments passed and the result returned.

The functools.wraps decorator is used to preserve the original function's metadata,
such as its name and docstring, when using the log_function_call decorator.
This ensures that the decorated function retains its identity and documentation.
'''

import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

@log_function_call
def multiply_numbers(x, y):
    """Multiply two numbers and return the result."""
    return x * y

# Testing the decorated functions
result_sum = add_numbers(3, 5)
# Output:
# Calling add_numbers with arguments: (3, 5), {}
# add_numbers returned: 8
result_product = multiply_numbers(2, 4)
# Output:
# Calling multiply_numbers with arguments: (2, 4), {}
# multiply_numbers returned: 8
