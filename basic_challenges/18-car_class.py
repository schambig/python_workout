#!/usr/bin/python3

class Car:
  def __init__(self, brand, model, year, mileage, state=False):
    self.brand = brand
    self.model = model
    self.year = year
    self.mileage = mileage
    self.state = state

  def turnOn(self):
    self.state = True


  def turnOff(self):
    self.state = False


  def drive(self, kilometers):
    if self.state == True:
      self.mileage += kilometers
    else:
      raise Exception('The vehicle is off')


toyota = Car("Toyota", "Corolla", 2023, 0)
toyota.turnOn()
toyota.drive(100)
print(toyota.mileage)

toyota = Car("Toyota", "Corolla", 2023, 0)
toyota.turnOff()
toyota.drive(100)
