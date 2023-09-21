'''
Ternary operator is a shorthand way of writing an if-else statement in a single line.
It provides a concise syntax for expressing conditional expressions.
The ternary operator is also known as the conditional expression.
'''

# General syntax
# value_if_true if condition else value_if_false

# Basic example
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result) # Odd

# We can also nest ternary operator
x = 10
result = "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(result)
