if True:
  print('debera ejecutarse') # Esto siempre se ejecuta pues la condicion es True

if False:
  print('nunca se ejecuta') # Esto nunca se ejecuta ya que la condicion es False

'''
pet = input('Cual es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')


stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')

'''

'''
number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')
'''

number = input("Ingrese un numero => ")

# Check if the user input is a float
if "." in number:
    print("Debe ingresar un numero entero.")
else:
    result = int(number) % 2
    if (result == 0):
      print('Es par')
    else:
      print('Es impar')

'''
try:
    number = int(input('Ingrese un numero => '))
    result = number % 2
    if (result == 0):
        print('Es par')
    else:
        print('Es impar')
except ValueError:
    print('Debe ingresar un numero entero.')
'''