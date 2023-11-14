#!/usr/bin/python3

# using one except keyword:
def calculate_average(numbers):
    try:
        if not numbers:
            raise ValueError('La lista está vacía')
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError('La lista contiene elementos no numéricos')
  
# using two except keywords:
def calculate_average2(numbers):
    try:
        # result = sum(numbers) / len(numbers)
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:  # consider 0 elements in the list -> 0/0
        raise ValueError("La lista está vacía")
    except TypeError:
        raise TypeError("La lista contiene elementos no numéricos")
    # else:
    #     return result
  

print(calculate_average2([1, 2, 3, 4, 5]))

print(calculate_average2([10, 20, 30, 40, 50]))

print(calculate_average2([]))

print(calculate_average2([1, 2, '3', 4, 5]))
