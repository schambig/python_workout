try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno' # This is a custom message
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')

# Python Try Except
# https://www.w3schools.com/python/python_try_except.asp