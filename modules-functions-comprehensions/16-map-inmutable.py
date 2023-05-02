# Original list of dictionaries
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

def add_taxes(item):
  new_item = item.copy() # Make a copy of the original list to modify
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Original list')
print(items)


# More about copy function:
# Python List copy() Method: https://www.w3schools.com/python/ref_list_copy.asp
# Python Dictionary copy() Method: https://www.w3schools.com/python/python_dictionaries_copy.asp
# Python Set copy() Method: https://www.w3schools.com/python/ref_set_copy.asp

# Shallow vs Deep Copying of Python Objects using 'copy module':
# https://realpython.com/copying-python-objects/