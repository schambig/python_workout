'''
In Python, you can provide default values for function parameters.
Default parameters allow you to specify a value that will be used if the function is called
without providing a value for that parameter.
This is particularly useful when you want a parameter to be optional,
and you want to provide a default behavior if a value is not supplied.
'''

def greet(name, greeting="Hello"):
    """This function greets the person with the specified greeting."""
    print(f"{greeting}, {name}!")

# Calling the function with and without providing a value for 'greeting'
greet("Alice")  # Uses the default greeting "Hello"
greet("Bob", "Good morning")  # Uses the provided greeting "Good morning"

'''
In the example above, the greet function has a default parameter greeting set to "Hello".
When the function is called with just the name parameter, it uses the default greeting.
However, if a second argument is provided, it overrides the default value.
'''

# Default parameters always go to the right
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

# By using the parameters names we can call them in any order
resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)
