#!/usr/bin/python3

# use `isinstance()` within the function:
def calculate_discounted_price(price, discount):
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)): 
    raise TypeError('El precio y el descuento deben ser números') 
  if price < 0 or discount < 0:
    raise ValueError('El precio y el descuento deben ser valores positivos')
  try:
    return price * (1 - discount)
  except:
    raise Exception('Ha ocurrido un error inesperado')
  

print(calculate_discounted_price(100, 0.2))

print(calculate_discounted_price(-50, 0.2))
