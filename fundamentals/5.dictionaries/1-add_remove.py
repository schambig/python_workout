'''
We can add new key-value pairs using the next syntax: dict['key'] = 'value'
We can dremove/delete a key-value pair using the `del` kwyword: del dict['key']
'''

elements = {}

elements['name'] = 'Salo' # create the key-value pair
elements[(1, 2, 3)] = 'The key is a tuple'
elements['course'] = 'Python'
elements['name'] = 'Kodama' # update the value created in line 8
print(elements)
# {'name': 'Kodama', (1, 2, 3): 'The key is a tuple', 'course': 'Python'}

# Remove key-value pairs with `del` keyword and pop() method
del elements['name'] # {(1, 2, 3): 'The key is a tuple', 'course': 'Python'}
elements.pop('course') # {(1, 2, 3): 'The key is a tuple'}
print(elements)

# Remove all key-value pairs in the dictionary
elements.clear()
print(elements) # {}

dic = {'a': 1, 'b': 2, 'c':3, 'a': 4} # same key with two values, takes last value
print(dic) # {'a': 4, 'b': 2, 'c': 3}
print(len(dic)) # 3
