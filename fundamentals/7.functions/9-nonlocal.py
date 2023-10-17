'''
The `nonlocal` keyword is used to indicate that a variable refers
to a variable in the nearest enclosing scope that is not global.
This is particularly useful when dealing with nested functions,
where you have a function defined inside another function.
'''

# Global and Local variables review
d = 'd'  # global variable

def funcion_principal():
    a = 'a'  # local variable for the whole function body/block
    b = 'b'  # local variable for the whole function body/block

    def funcion_anidada():
        c = 'c'  # local variable for `funcion_anidada()`

        # use `nonlocal` keyword to modify a local varible from a higher scope, if we don't
        # use `nonlocal` a new variable `b` will be created in a different memory space.
        nonlocal b
        b = 'Cambio de valor'

        print(a)  # a
        print(b)  # Cambio de valor
        print(id(b))  # 139716104259440

        print(d) # d

    funcion_anidada()
    # print(c)  # throw error because `c` is a local variable for `funcion_anidada()`
    print(b)  # Cambio de valor
    print(id(b))  #  139716104259440

funcion_principal()


# Example without using `nonlocal`
def outer_function():
    x = 10

    def inner_function():
        x = 5  # This creates a new local variable x, shadowing the outer x
        print("Inner Function:", x)

    inner_function()
    print("Outer Function:", x)

outer_function()

# In this example, the inner function creates a new local variable x,
# which shadows the outer variable x. As a result, the output is:
#   Inner Function: 5
#   Outer Function: 10

# Now, let's use nonlocal to modify the outer variable:
def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # Indicates that x refers to the outer x, not create a new local x
        x = 5
        print("Inner Function:", x)

    inner_function()
    print("Outer Function:", x)

outer_function()

# With the nonlocal keyword, the inner function now refers to
# the outer variable x instead of creating a new local variable. The output is:
#   Inner Function: 5
#   Outer Function: 5

'''
So, `nonlocal` is used to explicitly specify that a variable belongs to
an enclosing (non-global) scope,
allowing you to modify variables in an outer function's scope from within a nested function.
'''
