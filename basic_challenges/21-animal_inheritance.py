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
    return {
      'name': self.name,
      'age': self.age,
      'specie': self.specie,
      'hasFur': self.hasFur,
    }


bird = Animal('pepe', 1, 'bird')
pprint(bird.getInfo())

hippo = Mammal('bartolo', 3, 'hippo', False)
pprint(hippo.getInfo())
