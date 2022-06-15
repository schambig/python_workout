# En Python un float es una aproximacion, es por esi que si comparamos x e y
# tendremos con resultado False
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y) # Output: False

# Comparando flotantes casteando a string y limitando la precision decimal (fuerza bruta)
y_str = format(y, ".2g") # Usamos la funcion format() para castear a str y sleccionamos solo 2 cifras significativas
print('str =>', y_str)
print(y_str == str(x)) # Output: True

print('-' * 10)

print(y, x)

# Comparando flotantes de forma matematica, usando una tolerancia
tolerance = 0.00001
print(abs(x - y) < tolerance)

'''
Using a tolerance value allows us to determine whether two floating-point numbers are "close enough" to be considered equal.
The tolerance value represents the maximum allowable difference between the two values.
If the absolute difference between the two values is less than the tolerance value,
we consider the values to be equal.
'''