'''
Nested functions in Python are functions that are defined inside of other functions,
also known as inner functions.
These inner functions have access to the variables and scope of the outer function,
which can be useful for organizing code and creating closures.
'''

# Simple examples:
def outer_function(message):
  def inner_function():
    print(message)
  inner_function()

outer_function("Hello, world!")

def outer_function(x):
    def inner_function(y):
        return x + y
    
    result = inner_function(5)
    return result

output = outer_function(10)
print(output) # 15

# A simple bank transaction
def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):

        if cantidad <= balance:        
            return balance - cantidad
        else:
            return None

    print(id(cantidad))
    print(id(balance))

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado = operacion(10, 30, 'retiro')
print(resultado)
