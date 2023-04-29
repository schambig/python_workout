# Define a list of dictionaries
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
print(items) # Print the orginal list of dictionaries since map doesn't change the original list
print(prices) # [100, 300, 200]

'''
THIS ONLY WORKS IN PYTHON 3.9+
Here is an alternative way to do the same as using the add_taxes and map, but using lambda function (one liner)
The result will be the same as line 37 nad 62

  new_items = list(map(lambda x: x | {'tax': x['price'] * 0.19}, items)) 
  print(new_items) # Print the above list of dictionaries including the new taxes:value pair

The pipe operator is used to combine two dictionaries.
In this case, the first dictionary is the dictionary x, and the second dictionary is the dictionary {'tax': x['price'] * 0.19}.
The pipe operator creates a new dictionary that contains all of the key-value pairs from the first dictionary,
plus the key-value pair tax from the second dictionary.
The value of the tax key is calculated by multiplying the value of the price key by 0.19.
'''

# THIS WORKS IN PYTHON 3.9-
new_list = list(map(lambda item: {**item, **{'tax': item['price'] * 0.19}}, items))
print(new_list) # Print the original list of dictionaries including the new taxes:value pair
print(items) # Print original list of dictionaries since map doesn't change the original list
'''
The ** symbols are called unpacking operators. They are used to unpack the contents of a dictionary into keyword arguments.
In this case, the ** symbols unpack the contents of the dictionary item into keyword arguments for the {...} expression.
This means that the {...} expression will have access to all of the key-value pairs from the dictionary item.

The {...} expression is called a dict comprehension.
It is used to create a new dictionary from an iterable. In this case, the iterable is the dictionary item.
The dict comprehension will create a new dictionary that contains all of the key-value pairs from the dictionary item, plus the key-value pair tax.
The value of the tax key is calculated by multiplying the value of the price key by 0.19.
The map() function takes two arguments: a function and a iterable.
In this case, the function is the lambda expression lambda item: {**item, **{'tax': item['price'] * 0.19} and the iterable is the list items.
The lambda expression takes one argument, which is a dictionary representing an item.
The lambda expression then returns a new dictionary that is the same as the original dictionary, but with an additional key-value pair called tax.
The value of the tax key is calculated by multiplying the value of the price key by 0.19.
'''

# We need to define a function to pass it to map
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items) # Print the original list of dictionaries including the new taxes:value pair
print(items) # Print the same as the line above because add_taxes function modifies the original dictionary