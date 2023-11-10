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
