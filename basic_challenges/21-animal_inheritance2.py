#!/usr/bin/python3
from pprint import pprint


class Animal:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie


    def getInfo(self):
        ''' Instead of including the getInfo method in each class, only define it
            in the base class Animal.
            The getInfo method then utilizes the __dict__ attribute to create a
            dictionary representation of the object.
        '''
        return dict(**self.__dict__)


class Mammal(Animal):
    def __init__(self, name, age, specie, hasFur):
        super().__init__(name, age, specie)
        self.hasFur = hasFur
  

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, 'dog', True)  # set default values for parent attibutes
        self.breed = breed


    def bark(self):
        return 'woof!'
  

bird = Animal('pepe', 1, 'bird')
pprint(bird.getInfo())

hippo = Mammal('bartolo', 3, 'hippo', False)
pprint(hippo.getInfo())

dog = Dog('colitas', 3, 'chusquita')
pprint(dog.getInfo())
pprint(dog.bark())
