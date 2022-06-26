#not
print('NOT')
print('not True =>', not True)
print('not False =>', not False)
print()

# and
print('NOT AND')
print('not (True and True) =>', not (True and True))
print('not (True and False) =>', not (True and False))
print('not (False and True) =>', not (False and True))
print('not (False and False) =>', not (False and False))
print()

stock = input('Ingrese el numero de stock fuera del rango: 100 <= stock <= 1000 => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))