'''
Mutable data type!
Dictionaries are unordered, mutable, and can contain different data types.
A dictionary is a built-in data type that is used to store and manage
collections of key-value pairs.
It is also known as an associative array, map, or hash table in other
programming languages.
They are particularly useful when you need to associate data
with specific labels or identifiers.
'''

# We can difine a dictionary in two ways:
dictionary = {}
dictionary = dict()

# We can use different data type as key:
dictionary = {'total': 55, 10: 'Python Course', (1, 2, 3): True}
# keys:         string       int                 tuple

# Accessing Keys and Values:
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# keys = my_dict.keys() # Get a list of keys
# values = my_dict.values() # Get a list of values
# items = my_dict.items() # Get a list of key-value pairs as tuples

keys = diccionario.keys() # note that I;m not casting to tuple
print(keys) # dict_keys(['a', 'b', 'c', 'd']))

values = tuple(diccionario.values())
print(values) # (1, 2, 3, 4)

items = tuple(diccionario.items())
print(items) # (('a', 1), ('b', 2), ('c', 3), ('d', 4))
