'''
None is not a data type itself,

None is a special constant that represents the absence of a value or a null value.
It is a built-in singleton object of the NoneType class.
In other words, None is a unique object of its own type.

It's important to note that None is not the same as False or an empty string ('').
It is a distinct value representing the absence of a value or an undefined state.
'''

x = None
print(type(x))  # <class 'NoneType'>

# Functions without a specific return statement implicitly return None
def my_function():
    # No return statement, implicitly returns None
    pass

result = my_function()
print(result)  # None

# None is often used as a placeholder to indicate the absence of a meaningful value
# or to initialize variables before assigning them a specific value.
my_variable = None

# None is commonly used as a default value for function parameters to indicate that
# the argument is optional and not provided by the caller.
def my_function(arg=None):
    # Function logic
    pass

# Caller does not provide the argument
my_function()  
