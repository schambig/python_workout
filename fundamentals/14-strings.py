text = 'Ella sabe programar en Python'
print(text)
print()

'''
print('JavaScript' in text) # Output: False
print('Python' in text) # Output: True

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''
print('Funcion len:')
size = len(text)
print(size) # Output: 29
print()

print('Metodos upper, lower y count:')
print(text.upper()) # Output: ELLA SABE PROGRAMAR EN PYTHON
print(text.lower()) # Output: ella sabe programar en python
print(text.count('a')) # Output: 4
print()

print('Metodos swapcase, startswith, endswith y replace:')
print(text.swapcase()) # Output: eLLA SABE PROGRAMAR EN pYTHON
print(text.startswith('Ella')) # Output: True
print(text.endswith('Rust')) # Output: False
print(text.replace('Python', 'Go')) # Output: lla sabe programar en Go
print()

text_2 = 'este es un titulo'
print(text_2)
print()

print('Metodos capitalize, title, isdigit')
print(text_2.capitalize()) # Output: Este es un titulo
print(text_2.title()) # Output: Este Es Un Titulo
print(text_2.isdigit()) # Output: False
print()

print('Analizing "398" with .isdigit() function')
print("398".isdigit()) # Output: True