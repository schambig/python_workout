'''
index() method let us to get the index of a element in a list
note that this will return the index of the first occurrency of the element
If the element doesn't exist in the list we get an error
'''

lista = [8, 5, 90, 1, 5, 44, 132, 600, 3, 4, 5]

print(5 in lista)

index = lista.index(5)
print(index)
