'''
A docstring is a string literal that occurs as the first statement in
a module, function, class, or method definition. (4 documentable objects!!)
Its purpose is to provide documentation about the object it belongs to.
Docstrings are used to describe the purpose, usage, and behavior of the code
and are accessible through the __doc__ attribute or by using the help() function.
'''

# There are two common styles for docstrings in Python:

# Example with Triple-Quoted Strings:
def calculate_tax(income, tax_rate=0.15):
    """
    Calculate the tax amount based on the given income and tax rate.
   
    It can span multiple lines and provides information about the function.

    Parameters:
    - income (float): The income for which the tax needs to be calculated.
    - tax_rate (float, optional): The tax rate in decimal form (default is 0.15).

    Returns:
    float: The calculated tax amount.
    """
    tax_amount = income * tax_rate
    return tax_amount

print(calculate_tax.__doc__)


# Example with One-Line Strings:
def greet(name):
    """Greet the user with a personalized message.

    More detailed description, if necessary.

    Parameters:
    - name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}! Welcome to our platform."

print(greet.__doc__)
# print(help(greet)) # this will be shown in a extra window use `q` to quit
