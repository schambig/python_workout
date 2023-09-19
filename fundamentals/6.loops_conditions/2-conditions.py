'''
Conditions are expressions or statements that evaluate to either `True` or `False`.
Conditions are fundamental for controlling the flow of a program,
allowing you to make decisions based on whether certain conditions are met or not.
Conditions are used in conjunction with control flow statements like:
    if, else, and elif
to create branching and determine which block of code to execute.

Some common types of conditions in Python:
    1. Comparison Conditions: ==, !=, >, <, >=, <=
    2. Membership Conditions: in, not in
    3. Logical Conditions: and, or, not
    4. Identity Conditions: is, is not
    5. Truthiness and Falsiness: In Python, many values are considered "truthy"
                                (evaluate to True) or "falsy" (evaluate to False)
                                in a boolean context.
                                This includes values like 0, None,
                                empty sequences like: [], "", '', (), {}
                                and objects with a custom __bool__ or __len__ method.
'''

# Comparison Conditions:
x = 10
y = 5

if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

#  Membership Conditions:
my_list = [1, 2, 3, 4]

if 5 not in my_list:
    print("5 is not in the list")

# Logical Conditions:
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

# Identity Conditions:
a = [1, 2, 3]
b = [1, 2, 3]

if a is b:
    print("a and b refer to the same object")
else:
    print("a and b do not refer to the same object")

# Truthiness and Falsiness:
value = 0

if not value:
    print("The value is falsy")

'''
Conditions are crucial for writing dynamic and flexible programs,
allowing you to create logic that responds to different situations based on
the state of your data or variables.
They are used in conjunction with control flow statements to guide
the execution of code.
'''
