'''
Given strings are inmmutable in Python, we can't modify it
but we can generate a new one from existing ones
'''

name = 'Salomon'
name2 = 'Luis'

# Using + operator to concatenate
full_name = 'Mr. ' + name + ' ' + name2 + '.'

# Using % operator to concatenate
full_name2 = 'Mr. %s %s.' % (name, name2) 

# Using format() function
full_name3 = 'Mr. {} {}.'.format(name, name2) # {name} also works

# Using f-strings
full_name4 = f'Mr. {name} {name2}.'
 
print(full_name)
print(full_name2)
print(full_name3)
print(full_name4)
