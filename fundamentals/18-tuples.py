numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print('Tupla numbers =>', numbers) # Output: Tupla numbers => (1, 2, 3, 5)
print('numbers[0] =>', numbers[0]) # Output: numbers[0] => 1
print('numbers[-1] =>', numbers[-1]) # Output: numbers[-1] => 5
print('type(numbers) =>', type(numbers)) # Output: type(numbers) => <class 'tuple'>
print()

print('Tupla strings =>',strings) # Output: Tupla strings => ('nico', 'zule', 'santi', 'nico')
print('type(strings) =>', type(strings)) # Output: type(strings) => <class 'tuple'>

# CRUD
# numbers.append(10) AttributeError: 'tuple' object has no attibute 'append'
print(numbers) # Output: (1, 2, 3, 5)
# numbers[1] = 'change' TypeError: 'tuple' object does not support item assignment

# Metodos de tuplas
print(strings) # Output: ('nico', 'zule', 'santi', 'nico')
print(strings.index('zule')) # Output: 1
print(strings.count('nico')) # Output: 2

# Casteando una tupla a lista para poder aplicar metodos, pues la tupla es inmutable
my_list = list(strings)
print(my_list) # Output: ['nico', 'zule', 'santi', 'nico']
print(type(my_list)) # Output: <class 'list'>

my_list[1] = 'juli'
print(my_list) # Output: ['nico', 'juli', 'santi', 'nico']

# Casteando de lista a tupla luego de la modificacion
my_tuple = tuple(my_list)
print(my_tuple) # Output: ('nico', 'juli', 'santi', 'nico')