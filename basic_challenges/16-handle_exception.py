#!/usr/bin/python3

# use `isinstance()` within the function:
def calculate_discounted_price(price, discount):
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)): 
    raise TypeError('Price and discount must be numbers.') 
  if price < 0 or discount < 0:
    raise ValueError('Price and discount must be positive values.')
  try:
    return price * (1 - discount)
  except:
    raise Exception('An unexpected error has occurred.')

# use another function to manage instance type:
def calculate_discounted_price2(price, discount):
  if not is_instance(price) or not is_instance(discount):
    raise TypeError('Price and discount must be numbers.') 
  if price < 0 or discount < 0:
    raise ValueError('Price and discount must be positive values.')
  try:
    return price * (1 - discount)
  except:
    raise Exception('An unexpected error has occurred.')


def is_instance(element):
  if isinstance(element, (int, float)):
    return True
  return False


print(calculate_discounted_price(100, 0.2))

print(calculate_discounted_price(-50, 0.2))


'''Exeption class definition and example:
`Exception` is a built-in class that serves as the base class for all exceptions.
You can use it to catch any exception or create your own custom exceptions by
inheriting from it.

    try:
        # some code that may raise an exception
        result = 10 / 0
    except Exception as e:
        print(f"An exception occurred: {e}")
    
In this example, if an exception occurs during the execution of the code inside the try block,
the except block will catch it and print a message.
The Exception class here acts as a general catch-all for all exceptions.
'''
