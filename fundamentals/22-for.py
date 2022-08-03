'''
for element in range(1, 21): # 1: inclusive, 21: exclusive
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
print('Lista my_list:', my_list)
for element in my_list:
  print(element)
print()

my_tuple = ('salo', 'juli', 'santi')
print('Tupla my_tuple:', my_tuple)
for element in my_tuple:
  print(element)
print()

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
print('Diccionario Producto:', product)
for key in product:
  print(key, '=>', product[key])

for key, value in product.items(): # Retorna un array con key:value
  print(key, '=>', value)
print('product.items():', product.items())
print()

people = [
  {
    'name': 'grogu',
    'age': 150
  },
  {
    'name': 'din',
    'age': 45
  },
  {
    'name': 'bo-katan',
    'age': 35
  }
]

for person in people:
  print('name =>', person['name'])
  # print(person)
  # Output:
  #   {'name': 'grogu', 'age': 150}         
  #   {'name': 'din', 'age': 45}
  #   {'name': 'bo-katan', 'age': 35}