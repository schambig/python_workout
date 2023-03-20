
# dict = {}
# for i in range(1, 5):
#   dict[i] = i * 2

# print(dict) # {1: 2, 2: 4, 3: 6, 4: 8}

# dict_v2 = { i: i * 2 for i in range(1, 5)}
# print(dict_v2) # {1: 2, 2: 4, 3: 6, 4: 8}

# import random
# countries = ['col', 'mex', 'bol', 'pe']
# population = {}
# for country in countries:
#   population[country] = random.randint(1, 100)

# print(population) # {'col': 5, 'mex': 14, 'bol': 54, 'pe': 6}

# population_v2 = { country: random.randint(1, 100)  for country in countries}
# print(population_v2) # {'col': 36, 'mex': 46, 'bol': 5, 'pe': 31}

names = ['salo', 'lucy', 'jose']
ages = [99, 98, 97]

# The zip() function in Python is used to combine two or more iterables into a single iterable,
# where corresponding elements from the input iterables are paired together as tuples.
print(list(zip(names, ages))) # [('salo', 99), ('lucy', 98), ('jose', 97)]

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict) # {'salo': 99, 'lucy': 98, 'jose': 97}