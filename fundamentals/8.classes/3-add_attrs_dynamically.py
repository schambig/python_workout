'''
Using `setattr` and `dot notation` (also known as attribute assignment using the dot operator)
are two ways to dynamically add instance attributes to an object in Python AT RUNTIME.
Here are the main differences between them:
'''


'''Syntax:'''
'''setattr: It's a built-in function that takes three arguments:
the object, the attribute name as a string, and the attribute value.'''
setattr(object, attribute_name, attribute_value)

'''Dot notation: It directly uses the dot operator to assign a value to an attribute.'''
object.attribute_name = attribute_value


'''Readability:'''
'''setattr: Explicitly shows that you are dynamically setting an attribute using a function call.
This can be helpful for clarity, especially when attribute names are generated dynamically.'''
class Person:
    pass

# Dynamic attribute assignment using setattr
person = Person()
attribute_name = "name"
attribute_value = "John Doe"
setattr(person, attribute_name, attribute_value)

# Readability: Explicitly shows dynamic attribute assignment
print(person.name)

'''Dot notation: The assignment looks like regular attribute assignment,
making the code concise and potentially more readable when you know the attribute names
at the time of coding.'''
class Person:
    pass

# Dynamic attribute assignment using dot notation
person = Person()
person.name = "John Doe"

# Readability: Concise and looks like regular attribute assignment
print(person.name)


'''Flexibility:'''
'''setattr: Offers more flexibility, especially when attribute names are generated dynamically
or retrieved from external data sources.
You can construct the attribute name as a string and pass it to setattr.'''
class Person:
    pass

# Dynamic attribute assignment with dynamically generated name
person = Person()
attribute_name = "name_" + str(1)
attribute_value = "John Doe"
setattr(person, attribute_name, attribute_value)

# Flexibility: Allows dynamic construction of attribute names
print(person.name_1)

'''Dot notation: Requires knowing the attribute names at the time of writing the code.
It's less flexible when the attribute names are determined dynamically.'''
# Dot notation doesn't provide the same flexibility for dynamic attribute names
# This is a hypothetical example as dot notation requires knowing attribute names at compile-time
person = Person()
person.name_1 = "John Doe"  # Raises AttributeError if name_1 is not a valid attribute


'''Error Handling:'''
'''setattr: Since attribute names are provided as strings,
it allows for more dynamic handling and validation.
You can use conditional statements or try-except blocks to handle potential errors
related to attribute assignment.'''
class Person:
    pass

# Dynamic attribute assignment with error handling
person = Person()
attribute_name = "name"
attribute_value = "John Doe"

try:
    # Attempting to set an invalid attribute
    setattr(person, attribute_name, attribute_value)
except AttributeError as e:
    print(f"Error: {e}")

# Error Handling: Provides an opportunity to handle attribute-related errors

'''Dot notation: Errors related to attribute assignment can be less dynamically handled
since attribute names are fixed in the code.'''
# Dot notation might raise an AttributeError directly without specific error handling
person = Person()
person.invalid_attribute = "John Doe"  # Raises AttributeError if invalid_attribute is not a valid attribute


'''Consistency:'''
'''setattr: Provides a consistent interface for setting attributes,
whether the attribute names are known at compile-time or generated dynamically.
This consistency can be useful in certain scenarios.'''
class Person:
    pass

# Dynamic attribute assignment with consistency
person = Person()
attribute_name = "name"
attribute_value = "John Doe"
setattr(person, attribute_name, attribute_value)

# Consistency: Consistent interface for attribute assignment, whether dynamic or static
print(person.name)

'''Dot notation: Is more concise but relies on knowing the attribute names at the time of
writing the code.'''
class Person:
    pass

# Static attribute assignment with dot notation
person = Person()
person.name = "John Doe"

# Consistency: Looks similar to dynamic attribute assignment using dot notation
print(person.name)
