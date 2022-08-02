'''
while True: # Crea un bucle infinito
  print('se ejecuto')

counter = 0
while counter < 10:
  counter += 1
  print(counter)

counter = 0
while counter < 20:
  counter += 1
  if counter == 15:
    break # Termina el programa 
  print(counter)
'''

counter = 0
while counter < 20:
  counter += 1
  if counter < 15:
    continue # Salta automaticamente a la siguiente iteracion sin ejecutar el codigo que sigue
  print(counter)