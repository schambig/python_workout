'''
*args and **kwargs are used to allow a function to accept a variable number of arguments.
'''

'''
*args (Arbitrary Arguments):
    The *args in a function definition allows the function to accept any number of positional arguments.
    The *args syntax collects additional positional arguments into a tuple.
'''
def example_function(arg1, *args):
    print("First argument:", arg1)
    print("Additional arguments:", args)

example_function(1, 2, 3, 4)
# Output:
# First argument: 1
# Additional arguments: (2, 3, 4)

'''
**kwargs (Keyword Arguments):
    The **kwargs in a function definition allows the function to accept any number of keyword arguments.
    The **kwargs syntax collects additional keyword arguments into a dictionary.
'''
def example_function(arg1, **kwargs):
    print("First argument:", arg1)
    print("Additional keyword arguments:", kwargs)

example_function(1, key1="value1", key2="value2")
# Output:
# First argument: 1
# Additional keyword arguments: {'key1': 'value1', 'key2': 'value2'}

'''
Combining *args and **kwargs allows a function to accept any combination of positional and keyword arguments.
Here's an example:
'''
def example_function(arg1, *args, **kwargs):
    print("First argument:", arg1)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

example_function(1, 2, 3, key1="value1", key2="value2")
# Output:
# First argument: 1
# Additional positional arguments: (2, 3)
# Additional keyword arguments: {'key1': 'value1', 'key2': 'value2'}
