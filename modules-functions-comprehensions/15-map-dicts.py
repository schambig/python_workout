# Define a dictionary
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

prices = list(map(lambda item: item['price'], items))
print(items) # Print the above dictionary
print(prices) # [100, 300, 200]

# We need to define a function to pass it to map
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items) # Print the above dictionary including the new taxes:value pair
print(items) # Print the same as the line above because map modifies the original dictionary