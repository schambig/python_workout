text = "Ella sabe Python"
print('text:', text)
print()

print('INDEXING')
print('>' * 10)
print('Indice 0: ', text[0])
print('Indice 1: ',text[1])
# print(text[999]) Output: IndexError: string index out of range
print()

size = len(text)
print('size of text => ',size)
print('Accediendo al ultimo elemento usando: text[size - 1]')
print(text[size - 1])
print('Accediendo al ultimo elemento usando: text[-1]')
print(text[-1])
print('<' * 10)
print()

# slicing
print('SLICING')
print('>' * 10)
print('Slice text[0:5] :')
print(text[0:5])
print('Slice text[10:16] :')
print(text[10:16])
print('Slice text[:10] :')
print(text[:10])
print('Slice text[5:-1] :')
print(text[5:-1])
print('Slice text[5:]:')
print(text[5:])
print('Slice text[:] :')
print(text[:])
print('Slice text[10:16:1] :')
print(text[10:16:1])
print('Slice text[10:16:2] :')
print(text[10:16:2])
print('Slice text[::2] :')
print(text[::2])
print('Slice text[::-1], "Reverse" :')
print(text[::-1])
print('<' * 10)