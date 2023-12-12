#!/usr/bin/python3
from pprint import pprint


class Animal:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie


    def getInfo(self):
        return {
            'name': self.name,
            'age': self.age,
            'specie': self.specie,
        }


class Mammal(Animal):
    def __init__(self, name, age, specie, hasFur):  # add new class attribute
        super().__init__(name, age, specie)  # initialize Animal attributes
        self.hasFur = hasFur


    def getInfo(self):
        # return {
        #     'name': self.name,
        #     'age': self.age,
        #     'specie': self.specie,
        #     'hasFur': self.hasFur,
        # }

        # use super() to update the dictionary
        info = super().getInfo()
        # info['hasFur'] = self.hasFur
        # we can also use update() function instead of line above
        info.update({'hasFur': self.hasFur})
        return info
  

class Dog(Mammal):
    def __init__(self, name, age, breed, specie='dog', hasFur=True):
        super().__init__(name, age, specie, hasFur)
        self.breed = breed


    def getInfo(self):
        # return {
        #     'name': self.name,
        #     'age': self.age,
        #     'specie': self.specie,
        #     'hasFur': self.hasFur,
        #     'breed': self.breed,
        # } 
   
        # use super() to update the dictionary
        info = super().getInfo()
        # info['breed'] = self.breed
        # we can also use update() function instead of line above
        info.update({'breed': self.breed})
        return info


    def bark(self):
        return 'woof!'


bird = Animal('pepe', 1, 'bird')
pprint(bird.getInfo())

hippo = Mammal('bartolo', 3, 'hippo', False)
pprint(hippo.getInfo())

dog = Dog('colitas', 3, 'chusquita')
pprint(dog.getInfo())
pprint(dog.bark())
