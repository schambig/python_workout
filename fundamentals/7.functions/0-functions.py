'''
A function is a block of reusable code that performs a specific task or set of tasks.
Functions allow you to break down a program into smaller, more manageable pieces,
and they promote code reuse, making your code more modular and easier to understand.

Key characteristics of functions in Python:
    Modularity: Functions allow you to divide your code into smaller, modular units,
                making your program more organized and easier to manage.
    Reusability: Once a function is written, you can reuse it throughout your program or
                in other programs. This saves time and effort and reduces the risk of introducing errors.
    Data encapsulation: Functions can encapsulate data, hiding it from the rest of the program
                        and protecting it from accidental modification.
    Parameter passing: Functions can receive input data, known as parameters, which allows them
                        to be more versatile and adaptable to different situations.
    Return values: Functions can return output data, known as return values, which allows them
                    to be used to perform calculations or generate results.
'''

# Basic syntax for defining a function in Python:
def function_name(parameters):
    result = None
    # Code to be executed
    # ...
    return result  # Optional

# Simple function example
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# Calling the function
greet("Salo")
greet("Alice")
greet("Bob")

'''
In Python, the terms "parameter" and "argument" are often used interchangeably,
but they have slightly different meanings.
    Parameter: A parameter is a placeholder variable defined in the function's declaration.
                It represents the data that will be passed into the function when it is called.
    Argument: An argument is the actual value that is passed to the function when it is called.
                It replaces the placeholder variable (parameter) with a specific value.
In other words, parameters are like blueprints or templates for the data that the function will receive,
while arguments are the actual data that are provided to the function during its execution.
'''

# In this example, `name` is the parameter defined in the greet function's declaration.
# When the function is called with "Salo" as the argument,
# "Salo" becomes the actual value of the `name` parameter.
def greet(name):
    print("Hello, " + name + "!")

greet("Salo")
