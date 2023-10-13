'''
A lambda function is a concise way to create small, anonymous functions.
Lambda functions are also sometimes referred to as "anonymous functions"
or "lambda expressions."
Unlike regular functions defined with the `def` keyword, lambda functions
are defined using the `lambda` keyword.

The syntax for a lambda function is as follows:
    lambda <parameters>: <body of the function> (using parameters)
    lambda : True (no parameters)
    lambda p1=10, p2=20, p3=30 : p1 + p2 + p3 (default parameters)
    lambda *args, **kwargs: len(args) + len(kwargs) (Positional and keyword arguments)
'''

# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

# Using both functions
result1 = add(3, 5)
result2 = add_lambda(3, 5)

print(result1)  # 8
print(result2)  # 8

# Temperature convereter
funcion_grados = lambda grados : grados * 1.8 + 32
print(funcion_grados(10)) # 50.0

'''
Lambda functions are often used for short,
one-time operations where a full function definition might seem excessive.
They are especially useful in situations where you need to pass a simple function
as an argument to a higher-order function,
like in the case of functions like map(), filter(), or sorted().
'''
numbers = [1, 2, 3, 4, 5]

# Using a lambda function with map to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25]
