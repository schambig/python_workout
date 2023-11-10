'''
Method overloading and method overriding are related concepts in object-oriented programming,
but they are distinct and serve different purposes.
'''

'''
Method Overloading:
    In Python, method overloading is not supported in the traditional sense as it is in
    some other programming languages like Java or C++.
    However, you can achieve a form of method overloading by defining a single method with
    default values for some parameters or by using variable-length argument lists.
    Here's an example using default parameter values:
'''
class Calculator:
    def add(self, x, y=0, z=0):
        return x + y + z

# Creating an instance of the Calculator class
calc = Calculator()

# Different ways to call the add method
result1 = calc.add(1)          # x=1, y=0, z=0 (default values)
result2 = calc.add(1, 2)       # x=1, y=2, z=0 (default value for z)
result3 = calc.add(1, 2, 3)    # x=1, y=2, z=3

# Printing the results
print(result1)  # 1
print(result2)  # 3
print(result3)  # 6


'''
Method Overriding:
  - Method overriding occurs when a subclass provides a specific implementation for a method
    that is already defined in its superclass.
  - The method signature (name and parameters) in the subclass must match that of the method
    in the superclass.
  - The purpose is to provide a specialized implementation in the subclass,
    replacing or extending the behavior of the superclass method.
Example in Python:
'''
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()  # Woof!
cat.make_sound()  # Meow!


'''
In summary, method overloading involves defining multiple methods with
the same name in a class (NOT SUPPORTED IN PYTHON IN THE TRADITIONAL SENSE),
while method overriding involves providing a new implementation for a method in a subclass
that is already defined in its superclass.
Both concepts contribute to the flexibility and expressiveness of OOP languages.
'''
