'''
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class
to inherit attributes and methods from another class.
The class that is being inherited from is called the "parent class" or "base class,"
and the class that inherits is called the "child class" or "derived class."

The syntax for creating a child class that inherits from a parent class is as follows:
    class ParentClass:
        # Parent class attributes and methods

    class ChildClass(ParentClass):
        # Child class attributes and methods

Here's a brief explanation of how inheritance works in Python:
  - The child class inherits all the attributes and methods of the parent class.
  - The child class can also have additional attributes and methods or override the inherited ones.
  - If a method is defined in both the parent and the child class with the same name,
  the method in the child class will override the one in the parent class. This is known as method overriding.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be overridden in subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of the child classes
dog_instance = Dog("Pequeña")
cat_instance = Cat("Garfilito")

# Using the inherited methods
print(dog_instance.speak())  # Woof!
print(cat_instance.speak())  # Meow!

'''
In this example, the Dog and Cat classes inherit from the Animal class.
They both have a speak method, which overrides the abstract speak method in the Animal class.

Inheritance in Python provides a way to create a hierarchy of classes, promoting code reuse,
and making it easier to structure and organize your code.
'''


'''MULTIPLE INHERITANCE
The syntax for multiple inheritance is as follows:
    class ParentClass1:
        # Attributes and methods of the first parent class

    class ParentClass2:
        # Attributes and methods of the second parent class

    class ChildClass(ParentClass1, ParentClass2):
        # Attributes and methods of the child class
'''

class Animal:
    def make_sound(self):
        pass  # Abstract method, to be overridden in subclasses

class Mammal:
    def feed_milk(self):
        return "Feeding milk"

class Dog(Animal, Mammal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal, Mammal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the child classes
dog_instance = Dog()
cat_instance = Cat()

# Using the inherited methods
print(dog_instance.make_sound())  # Woof!
print(dog_instance.feed_milk())  # Feeding milk

print(cat_instance.make_sound())  # Meow!
print(cat_instance.feed_milk())  # OFeeding milk

'''
While multiple inheritance can be a powerful feature, it can also lead to complexities
and challenges, such as the "diamond problem".
Exercise caution and consider alternatives, such as composition,
when designing your class hierarchy to maintain code readability and avoid potential issues.
'''

# ===============================================================================

'''THE DIAMOND PROBLEM
The "diamond problem" is a term used in the context of object-oriented programming
to describe a particular issue that can arise with multiple inheritance.
The problem occurs when a class inherits from two classes that have a common ancestor.
This creates an ambiguity in the inheritance hierarchy, especially when methods or attributes
from the common ancestor are overridden in both parent classes.

Let's illustrate the diamond problem with a simple example:
'''

class A:
    def method(self):
        print("Method of class A")

class B(A):
    def method(self):
        print("Method of class B")

class C(A):
    def method(self):
        print("Method of class C")

class D(B, C):
    pass

# Creating an instance of class D
d_instance = D()

# Calling the method
d_instance.method()

'''
In this example, class D inherits from both class B and class C,
both of which, in turn, inherit from class A.
When you create an instance of class D and call the method,
it raises the diamond problem because it's ambiguous which method should be invoked—
the one from class B or class C.

This ambiguity can lead to unexpected behavior and make the code harder to understand
and maintain.
To address the diamond problem, programming languages and developers employ various solutions,
including:
  - Method Resolution Order (MRO): Languages like Python have a defined order in which
    they look for methods in the inheritance hierarchy.
    Python uses the C3 linearization algorithm to determine the MRO.
  - Virtual Inheritance: Some programming languages, like C++, provide a mechanism
    called "virtual inheritance" to avoid creating multiple instances of a common base class
    when multiple inheritance is involved.
  - Composition over Inheritance: In some cases, it might be better to use composition
    (combining objects) instead of inheritance to avoid the complexities associated
    with the diamond problem.
'''
