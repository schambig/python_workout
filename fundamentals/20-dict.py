# Diccionarios, insercion y actualizacion

person = {
  'name': 'salo',
  'last_name': 'chambi',
  'langs': ['python', 'javascript'],
  'age': 99
}

print('Dicionario person:')
print(person) # Output: {'name': 'salo', 'last_name': 'chambi', 'langs': ['python', 'javascript'], 'age': 99}
print()

print('Actualizando valores del diccionario:')
# Si el par llave:valor no existe, este es creado
person['name'] = 'luis'
person['age'] -= 50
person['langs'].append('rust')
print(person) # Output: {'name': 'luis', 'last_name': 'chambi', 'langs': ['python', 'javascript', 'rust'], 'age': 49}
print()

# Eliminando del diccionario usando keys
print('Eliminando valores del diccionario:')
del person['last_name']
person.pop('age')
print(person) # Output: {'name': 'luis', 'langs': ['python', 'javascript', 'rust']}
print()


print('Metodo .items() :')
print(person.items()) # Output: dict_items([('name', 'luis'), ('langs', ['python', 'javascript', 'rust'])])

print('Metodo .keys() :')
print(person.keys()) # Output: dict_keys(['name', 'langs'])

print('Metodo .values() :')
print(person.values()) # Output: dict_values(['luis', ['python', 'javascript', 'rust']])