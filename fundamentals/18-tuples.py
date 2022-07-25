numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print('Tupla numbers =>', numbers)
print('numbers[0] =>', numbers[0])
print('numbers[-1] =>', numbers[-1])
print('type(numbers) =>', type(numbers))
print()

print('Tupla strings =>',strings)
print('type(strings) =>', type(strings))

# CRUD
# numbers.append(10) AttributeError: 'tuple' object has no attibute 'append'
print(numbers)
# numbers[1] = 'change' TypeError: 'tuple' object does not support item assignment

# Metodos de tuplas
print(strings)
print(strings.index('zule')) # Output: 1
print(strings.count('nico')) # Output: 2

# Casteando una tupla a lista para poder aplicar metodos, pues la tupla es inmutable
my_list = list(strings)
print(my_list)
print(type(my_list)) # Output: <class 'list'>

my_list[1] = 'juli'
print(my_list)

# Casteando de lista a tupla luego de la modificacion
my_tuple = tuple(my_list)
print(my_tuple)