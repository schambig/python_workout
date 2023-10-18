'''
`doctest` is a module in the Python standard library that can be used to extract and run tests
from docstrings.
Here's how you can use doctest for testing docstrings:
'''
def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The sum of the two numbers.

    Docstring tests:
    >>> add_numbers(2, 3)
    5

    >>> add_numbers(-1, 1)
    0

    >>> add_numbers(5, 8)
    13
    """
    return a + b

# from the cli run: python3 -m doctest 16-docstring.py
# if everything is ok no errors will be shown.
