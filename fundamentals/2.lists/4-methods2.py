'''
sort() function lets us to sort/order the list elements
it orders the list in ascendet order by default
min() gets the minimun value in a list
max() gets the maximun value in a list
`in` keyword lets us know if an element is included in a list
`not in` kinda the same as above but the opposite, checks if a element is not in the list
'''

lista = [100, 50, 25, 600, 3, 0, -1]

# Sort the list in ascendent order by default
lista.sort()

# Sort the list in descendent order
lista.sort(reverse=True)

# Sort the list ascendent order by default and get the first(min) and last(max) elements
lista.sort()
print(lista)
print(lista[0]) # min
print(lista[-1]) # max

# Get the min and max values in a list, no need to sort and indexes
print(min(lista)) # min
print(max(lista)) # max

# Look for an element in a list, we'll get a boolean value as response
print(9 in lista)
print('Found it!' if 9 in lista else 'Keep trying!')
print(25 in lista)
