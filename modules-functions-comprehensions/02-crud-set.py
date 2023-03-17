set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size) # output: 3

print('col' in set_countries) # output: True
print('pe' in set_countries) # output: False

# add
set_countries.add('pe') 
print(set_countries) # output: {'mex', 'bol', 'col', 'pe'} 
set_countries.add('pe')
print(set_countries) # output: {'mex', 'bol', 'col', 'pe'}

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries) # output: {'ar', 'mex', 'ecua', 'col', 'pe', 'bol'}

# remove

set_countries.remove('col')
print(set_countries) # output: {'ar', 'mex', 'ecua', 'pe', 'bol'} 

set_countries.remove('ar')
# set_countries.remove('arg') # output:
# Traceback (most recent call last):
#   File "/home/salomon/githubRepos/python_workout/modules-functions-comprehensions/02-crud-set.py", line 25, in <module>
#     set_countries.remove('arg')
# KeyError: 'arg'
set_countries.discard('arg')
print(set_countries) # output: {'mex', 'ecua', 'bol', 'pe'}
set_countries.add('arg')
print(set_countries) # output: {'arg', 'mex', 'ecua', 'bol', 'pe'}
set_countries.clear() # Elimina todo el contenido del set
print(set_countries) # output: set() 
print(len(set_countries)) # output: 0