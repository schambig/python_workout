'''
A decorator is a special type of function that is used to modify or extend
the behavior of another function or method.
Decorators are commonly used to wrap or enhance the functionality of functions without
modifying their actual code.
They provide a way to separate concerns and make code more modular and reusable.

The syntax for using decorators involves placing the decorator symbol @ followed by
the decorator function name above the function definition.
Here's a simple example:
    @my_decorator
    def my_function():
        # function code here
        pass
'''
'''
a -> Decorator function
b -> Function to decorate
c -> 'Decorated function'

a(b) -> c
'''
def function_a(function_b):

    def function_c():
        print('Before calling function_b')

        function_b()

        print('After calling function_b')

    return function_c

# Using the decorator function
@function_a
def greeting():
    print('Hello from greeting function')

# greeting()
# Output:
# Before calling function_b
# Hello from greeting function
# After calling function_b

# Using the decorator on another function
@function_a
def sum():
    print(10 + 30)

sum()
# Output:
# Before calling function_b
# 40
# After calling function_b

'''
Analogy: The Coffee Shop Decorator
    Imagine you're the owner of a coffee shop, and you have different types of coffee
    that customers can order.
    Each type of coffee is like a function, and you want to add some extra service or decoration
    to certain types of coffee.
    Now, instead of modifying the recipe (function) for each type of coffee,
    you decide to use decorators.
'''

# 1.Plain Coffee (Original Function):
#   Your basic coffee is just plain black coffee.
def plain_coffee():
    return "Black Coffee"

# 2.Decorator: Adding Sugar (Decorator Function):
#   You create a decorator to add sugar to any coffee.
def add_sugar(coffee_function):
    def wrapper():
        return coffee_function() + " with Sugar"
    return wrapper

# 3.Decorate a Coffee Type (Apply Decorator):
#   Now, you decorate your plain coffee function with the add_sugar decorator.
@add_sugar
def plain_coffee():
    return "Black Coffee"

# 4.Serve Decorated Coffee (Call Decorated Function):
#   When a customer orders plain coffee, you serve them the decorated version.
print(plain_coffee())  # Black Coffee with Sugar

'''
`plain_coffee` is like a basic function representing black coffee.
`add_sugar` is a decorator function that takes another function (coffee_function) and returns
a new function (`wrapper`) that adds sugar to the result of the original function.
`@add_sugar` is like applying the decorator to the `plain_coffee` function.
When you call `plain_coffee()`, you're actually calling the decorated version that includes
the sugar.
In this analogy, the decorator (`add_sugar`) is a reusable way to enhance the behavior
of different types of coffee (functions) without modifying their original recipes.
You can have other decorators (`add_milk`, `add_caramel`) to modify the coffee in different ways,
and you can mix and match these decorators as needed.
This helps keep your coffee recipes (functions) clean and modular.
'''
