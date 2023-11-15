#!/usr/bin/python3

# using one except keyword:
def calculate_average(numbers):
    try:
        if not numbers:
            raise ValueError('The list is empty.')
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError('The list contains non-numeric elements.')
  
# using two except keywords:
def calculate_average2(numbers):
    try:
        # result = sum(numbers) / len(numbers)
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:  # consider 0 elements in the list -> 0/0
        raise ValueError('The list is empty.')
    except TypeError:
        raise TypeError('The list contains non-numeric elements.')
    # else:
    #     return result
  

print(calculate_average([1, 2, 3, 4, 5]))

print(calculate_average([10, 20, 30, 40, 50]))

print(calculate_average([]))

print(calculate_average([1, 2, '3', 4, 5]))
