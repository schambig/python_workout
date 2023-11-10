'''
The `super()` function in Python is used to call methods and access attributes of
a superclass (parent class) in a class hierarchy.
It provides a way to delegate method calls to the superclass, allowing for
cooperative multiple inheritance and maintaining a consistent method resolution order (MRO).
'''

'''
Suppose we are building a set of classes to represent animals in a zoo.
We start with a generic Animal class and then create specific classes for different
types of animals, such as Bird, Mammal, and Reptile.
Each of these subclasses will have its own implementation of a make_sound method.
'''

'''1. Basic Animal Class:'''
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

# Creating an instance of the Animal class
generic_animal = Animal(name="Generic Animal")
generic_animal.make_sound()  # Generic animal sound

'''2. Subclasses: Bird, Mammal, Reptile'''
class Bird(Animal):
    def make_sound(self):
        print("Tweet tweet")

class Mammal(Animal):
    def make_sound(self):
        print("Mammal sound")

class Reptile(Animal):
    def make_sound(self):
        print("Hiss")

'''
Now, let's say we want to create a Parrot class, which is a specific type of bird.
We want the Parrot class to inherit from both the Bird class and the Mammal class
(don't worry about the biological accuracy; this is just an illustrative example).
We'll use super() to make sure we call the make_sound method of both the Bird and Mammal classes.
'''

'''3. Using super() in Parrot Class:'''
class Parrot(Bird, Mammal):
    def make_sound(self):
        print("Squawk")
        super().make_sound()  # call the method in its immediate parent
        # super(Bird, self).make_sound()  # Call make_sound from Bird
        # super(Mammal, self).make_sound()  # Call make_sound from Mammal directly
        Mammal.make_sound(self)  # Call make_sound from Mammal

# Creating an instance of the Parrot class
parrot = Parrot(name="Polly")
parrot.make_sound()
# Output:
# Squawk
# Tweet tweet
# Mammal sound

'''
In this example:
    The Parrot class inherits from both Bird and Mammal.
    The make_sound method in Parrot first prints the specific sound of a parrot ("Squawk")
    and then uses super().make_sound() to call the make_sound method of Bird,
    and then we call the make_sound() from Mammal directly.
'''
