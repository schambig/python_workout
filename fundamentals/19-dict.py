my_dict = {}
print('type(my_dict) =>', type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Salomon',
  'last_name': 'Chambi Gutierrez',
  'age': 99
}
print()

print('my_dict =>', my_dict)
print('len(my_dict) =>', len(my_dict))
print()

print("my_dict['age'] =>", my_dict['age'])
print("my_dict['last_name'] =>", my_dict['last_name'])
print("my_dict.get('age') =>", my_dict.get('age'))
print()

print("'avion' in my_dict =>", 'avion' in my_dict) # Output: True
print("'otroqueno' in my_dict =>", 'otroqueno' in my_dict) # Output: False