'''
for element in range(1, 21): # 1: inclusive, 21: exclusive
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
print(my_list) # Output: [23, 45, 67, 89, 43]
for element in my_list:
  print(element)
# Output:
# 23
# 45
# 67
# 89
# 43 
print()

my_tuple = ('salo', 'juli', 'santi')
print(my_tuple) # Output: ('salo', 'juli', 'santi')
for element in my_tuple:
  print(element)
# Output: 
# salo
# juli
# santi
print()

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
print(product) # Output: {'name': 'Camisa', 'price': 100, 'stock': 89}
for key in product:
  print(key, '=>', product[key])
# Output: 
# name => Camisa
# price => 100
# stock => 89
for key, value in product.items():
  print(key, '=>', value)
# Output: 
# name => Camisa
# price => 100
# stock => 89
print(product.items()) # Output: dict_items([('name', 'Camisa'), ('price', 100), ('stock', 89)])
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
  # Output:
  # name => grogu
  # name => din
  # name => bo-katan

for person in people:
  print(person)
  # Output:
  #   {'name': 'grogu', 'age': 150}         
  #   {'name': 'din', 'age': 45}
  #   {'name': 'bo-katan', 'age': 35}