# Diccionarios, definincion y lectura

my_dict = {}
print(type(my_dict)) # Output: <class 'dict'>

my_dict = {
  'avion': "bla bla bla",
  'name': 'Salomon',
  'last_name': 'Chambi Gutierrez',
  'age': 99
}
print()

print(my_dict) # Output: {'avion': 'bla bla bla', 'name': 'Salomon', 'last_name': 'Chambi Gutierrez', 'age': 99}
print(len(my_dict)) # Output: 4
print()

print(my_dict['age']) # Output: 99
print(my_dict['last_name']) # Output: Chambi Gutierrez
print(my_dict.get('age')) # Output: 99
print()

print('avion' in my_dict) # Output: True
print('otroqueno' in my_dict) # Output: False