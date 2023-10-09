'''
The term "scope" refers to the region of a program where a particular identifier
(such as a variable or function name) is valid and can be used.
The concept of scope is essential for understanding how variables are accessed
and modified within different parts of a program.
'''

animal = 'León' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    # global animal # we use global keyword to midify the global variable
    animal = 'Ballena' # Variable Local
    tipo = 'Mamifero' # Variable Local

    print(animal)
    print(id(animal))
    
imprimir_animal()

print(animal)
print(id(animal))
# print(tipo) # only exists within imprimir_animal() function so we get an error


'''
There are two main types of scope in Python:

Global Scope:
Variables defined outside of any function or block have a global scope.
They can be accessed from any part of the program, including both inside and outside functions.
To create a global variable, you simply define it outside of any function or block.
'''
global_variable = 10

def my_function():
    print(global_variable)

my_function()  # 10

'''
Local Scope:
Variables defined inside a function have a local scope.
They are only accessible within that specific function.
When a function is called, a new local scope is created,
and any variables defined within that function are only valid within that scope.
'''
def my_function():
    local_variable = 20
    print(local_variable)

my_function()  # 20

# Attempting to access the local_variable outside the function will result in an error
# print(local_variable)  # Raises NameError

'''
In addition to variables, functions also have scope.
Functions defined inside other functions have a local scope
and are only accessible within the enclosing function.
'''
def outer_function():
    outer_variable = 30

    def inner_function():
        print(outer_variable)

    inner_function()

outer_function()  # 30
