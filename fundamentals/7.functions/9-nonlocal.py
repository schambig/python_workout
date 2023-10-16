'''
A closure is a nested function that captures and remembers the values in the enclosing
function's local scope, even if the outer function has finished executing.
The closure "closes over" the variables it references,
meaning it retains access to those variables even after the outer function has completed
its execution.
This behavior allows the inner function to access and manipulate the values of
the outer function's local variables.
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
