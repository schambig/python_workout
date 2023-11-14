#!/usr/bin/python3

def calculate_average(numbers):
  try:
    if not numbers:
      raise ValueError('La lista está vacía')
    return sum(numbers) / len(numbers)
  except TypeError:
      raise TypeError('La lista contiene elementos no numéricos')
  

print(calculate_average([1, 2, 3, 4, 5]))

print(calculate_average([10, 20, 30, 40, 50]))

print(calculate_average([]))

print(calculate_average([1, 2, '3', 4, 5]))
