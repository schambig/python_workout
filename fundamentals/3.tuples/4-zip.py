'''
zip() is a built-in function that takes two or more iterables
(such as lists or tuples) and pairs the elements at corresponding positions,
creating an iterator of tuples.
This is particularly useful when you want to iterate over multiple sequences simultaneously.
'''

lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500, 600, 700]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # returns a zip object (location at memory)
resultado = tuple(resultado) # casting zip object into a tuple o tuples

print(resultado)
#((1, 10, 100, 1000), (2, 20, 200, 2000), (3, 30, 300, 3000), (4, 40, 400, 4000), (5, 50, 500, 5000))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Using zip to pair elements from two lists
zipped_data = zip(names, ages)

# Converting the zip object to a list for display
result_list = list(zipped_data)

print(result_list) # [('Alice', 25), ('Bob', 30), ('Charlie', 22)]


# You can also use zip with more than two iterables:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
scores = [90, 85, 95]

# Using zip to pair elements from three lists
zipped_data = zip(names, ages, scores)

# Converting the zip object to a list for display
result_list = list(zipped_data)

print(result_list) # [('Alice', 25, 90), ('Bob', 30, 85), ('Charlie', 22, 95)]


# You can also use zip in a loop for simultaneous iteration:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Using zip in a loop for simultaneous iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
    # Alice is 25 years old.
    # Bob is 30 years old.
    # Charlie is 22 years old.

'''
Keep in mind that if the iterables passed to zip are of different lengths,
zip stops creating tuples when the shortest input iterable is exhausted.
'''
