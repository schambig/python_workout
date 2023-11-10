'''
Methods inside a class are functions defined within the scope of that class.
These methods define the behavior of instances created from the class.
Methods can access and modify the attributes of the instances, perform operations,
and interact with other methods within the same class.

There are two main types of methods in a class:
    Instance methods
    Class methods
'''

'''INSTANCE METHODS:
    Instance methods are the most common type of methods in a class.
    They operate on an instance of the class and have access to its attributes.
    The first parameter of an instance method is always self, which refers to the instance (object) the method is called on.
    Instance methods can be called on an instance of the class.'''
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog(name="Colitas")
# Calling an instance method
my_dog.bark()  # Colitas says Woof!


'''CLASS METHODS:
    Class methods are marked with the @classmethod decorator.
    They operate on the class itself and have access to class-level attributes.
    The first parameter of a class method is conventionally named cls, referring to the class.
    Class methods can be called on the class itself, not on instances.'''
class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def print_class_attribute(cls):
        print(cls.class_attribute)

# Calling a class method
MyClass.print_class_attribute()  # I am a class attribute

# Another example of Class method
class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)  # 615.752032


'''Here's a brief example that includes both instance and class methods:'''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")

    @classmethod
    def show_class_info(cls):
        print(f"This is the {cls.__name__} class")

# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry")

# Calling instance methods
my_car.display_info()  # Toyota Camry

# Calling class methods
Car.show_class_info()  # This is the Car class

'''
In this example, display_info is an instance method that operates on an instance
of the Car class, while show_class_info is a class method that operates on the class itself.
'''
