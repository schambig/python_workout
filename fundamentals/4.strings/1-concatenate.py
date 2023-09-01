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

# Using format() function, in 2nd form we can manipulate the variables order
full_name3 = 'Mr. {} {}.'.format(name, name2)
full_name3 = 'Mr. {nombre2} {nombre}.'.format(nombre=name, 
                                              nombre2=name2)

# Using f-strings, we can also put expressions inside the {}
full_name4 = f'Mr. {name} {name2}.\n{"#" * 20}\n{10 * 20}'
 
print(full_name)
print(full_name2)
print(full_name3) # Mr. Luis Salomon.
print(full_name4) # Mr. Salomon Luis.
                  # ####################
                  # 200
