'''
A closure is a nested function that captures and remembers the values in the enclosing
function's local scope, even if the outer function has finished executing.
The closure "closes over" the variables it references,
meaning it retains access to those variables even after the outer function has completed
its execution.
This behavior allows the inner function to access and manipulate the values of
the outer function's local variables.
'''

# `mostrar_mensaje()` is a closure function since it captures and remembers/retains
# access to the local variable `message`from the outer function `saludar()`
def saludar(username):
    mensaje = f'Hola {username}'  # Local variable

    def mostrar_mensaje(): # Nested function
        print(mensaje)

    return mostrar_mensaje

username = 'Haku'
respuesta = saludar(username)

username = 'Salomon'  # even if we change the variable's value it retains 'Haku'

respuesta()  # Hola Haku
respuesta()  # Hola Haku
respuesta()  # Hola Haku


# Another example of a closure function:
def outer_function(x):
    # Inner function, which is a closure
    def inner_function(y):
        return x + y
    
    return inner_function

# Create a closure
closure_instance = outer_function(10)

# Use the closure
result = closure_instance(5)
print(result)  # 15

'''
`outer_function` takes an argument x and defines an inner function `inner_function`.
`inner_function` is a closure because it references the variable `x` from the outer function.
The closure retains access to x even after `outer_function` has completed.
`outer_function(10)` returns an instance of the closure, effectively "closing over" the value 10.
`closure_instance(5)` then uses the closure to add 5 to the captured value of x,
resulting in the output 15.
'''
