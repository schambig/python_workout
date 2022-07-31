# Diccionarios, insercion y actualizacion

person = {
  'name': 'salo',
  'last_name': 'chambi',
  'langs': ['python', 'javascript'],
  'age': 99
}

print('Dicionario person:')
print(person)
print()

print('Actualizando valores del diccionario:')
person['name'] = 'luis'
person['age'] -= 50
person['langs'].append('rust')
print(person)
print()

# Eliminando del diccionario usando keys
print('Eliminando valores del diccionario:')
del person['last_name']
person.pop('age')
print('person =>', person)
print()


print('Metodo .items() :')
print(person.items())

print('Metodo .keys() :')
print(person.keys())

print('Metodo .values() :')
print(person.values())