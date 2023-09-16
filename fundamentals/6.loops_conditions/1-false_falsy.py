'''
In Python, the primary way to represent the Boolean value False is by using
the built-in constant False.
However, there are other values that are considered "falsy" in a Boolean context,
meaning they are treated as equivalent to False when used in conditions.
Here are some of them:
'''

# The False Constant:
my_variable = False

# Numeric Zero: Numeric values of 0 (integer or float) are considered falsy.
my_variable = 0
my_variable = 0.0

# Empty Sequences:
# Like empty strings, lists, tuples, and dictionaries are considered falsy.
empty_string = "" or ''
empty_list = []
empty_tuple = ()
empty_dict = {}

# The None constant is considered falsy.
my_variable = None

# Expressions that evaluate to False in comparison operations are obviously falsy.
result = (2 == 3)  # result is False

# Useful way to proof flasy
value = 0

if not value:
    print("The value is falsy")
