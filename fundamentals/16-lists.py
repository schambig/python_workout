numbers = [1, 2, 3, 4]
print('Lista numbers: ', numbers)
print(type(numbers))
print()

tasks = ['make a dishes', 'play videogames']
print('Lista tasks: ', tasks)
print()

types = [1, True, 'hola']
print('Lista types: ', types)
print()

print('Accediendo a numbers[0]: ')
print(numbers[0])
print('Accediendo a tasks[0]: ')
print(tasks[0])
print()

text = 'Hola'
# text[0] = 'W' Output: TypeError: 'str' object does not support item assignment

print('Reemplazando tasks[0]:')
tasks[0] = 'watch platzi courses'
print(tasks)
print()

print('Reemplazando nuevamente tasks[0]:')
tasks[0] = 'do the dishes'
print(tasks)
print()

print('Slicing la lista numbers[:3] :')
print(numbers[:3])
print()

print('True in types: ', True in types) # Output: True
print("'hola' in types",'hola' in types) # Output: True