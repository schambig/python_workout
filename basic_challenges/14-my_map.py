#!/usr/bin/python3

# One liner
def my_map(lista, func):
  return list(map(func, lista))

# Using list comprehension
def my_map2(lista, func):
    return [func(item) for item in lista]

# Using a loop
def my_map3(lista, func):
    out = []
    for i in lista:
        out.append(func(i))
    return out


print(my_map([1, 2, 3, 4], lambda num: num * 2))

print(my_map([
{"name": "colas", "age": 3},
{"name": "pequeña", "age": 4},
{"name": "blanca", "age": 3},
{"name": "manchas", "age": 2}],
lambda pet: pet["name"]))
