set_countries = {'per', 'col', 'ar'}
print(set_countries) # output: {'col', 'ar', 'per'}
print(type(set_countries)) # output: <class 'set'>

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers) # output: {1, 2, 443, 23}

set_types = {1, 'hola', False, 12.12}
print(set_types) # output: {False, 1, 'hola', 12.12}

set_from_string = set('hoola') # cast to set (no duplicates)
print(set_from_string) # output: {'l', 'h', 'o', 'a'}

set_from_tuples = set(('abc', 'cbv', 'as', 'abc')) # cast to set (no duplicates)
print(set_from_tuples) # output: {'as', 'cbv', 'abc'}

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers) # cast to set (no duplicates)
print(set_numbers) # output: {1, 2, 3, 4} 
unique_numbers = list(set_numbers) # cast to list
print(unique_numbers) # output: [1, 2, 3, 4]

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# More infor about sets: https://www.w3schools.com/python/python_sets.asp