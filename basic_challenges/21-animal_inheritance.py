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


bird = Animal('pepe', 1, 'bird')
pprint(bird.getInfo())
