'''
`or` keyword can be used for a specific purpose in the context of variable assignment.
It is often used in a concise way to assign a default value to a variable
if the variable is currently assigned a falsy value (None, 0, empty sequences, etc.).
'''

# This will check from left to right and if it find a `falsy` value y assing the next `truthy` value
# Remember all the values that are considered 'falsy' in a boolean context
x = None or '' or 0 or [] or {} or ()
y = x or "Default Value"
print(y)  # Default Value

variable = 0.0 or 'Luis'
print(variable) # Luis

lista = [] # this is a `falsy` value equivalent to False
name = 'Salo'

if lista: # this will be treated as False
    var = lista
else:
    var = name

# The above can be one line
var2 = lista or name

print(var) # Salo
print(var2) # Salo

'''
Keep in mind that this method might not be suitable for all cases,
especially when the variable can have falsy values that are not intended to be replaced
by the default value. In such cases, it's better to use an explicit if-else statement for clarity.
'''
x = 0
y = "Default Value" if x is None else x
print(y)  # 0
