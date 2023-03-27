print('Hola') # Hola

def my_print(text):
  print(text * 2)

my_print('Este es my texto ') # Este es mi texto Este es mi texto
my_print('Hola ') # Hola Hola

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b) # We are using a function inside another

suma(1, 5) # (1 + 5) * 2 = 12
suma(10, 4) # (10 + 4) * 2 = 28
  
# More info about functions:
# https://www.w3schools.com/python/python_functions.asp

# Arbitrary Arguments, *args
#   def my_function(*kids):
#   print("The youngest child is " + kids[2])

#   my_function("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
#   def my_function(**kid):
#     print("His last name is " + kid["lname"])

#   my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
#   def my_function(country = "Norway"):
#     print("I am from " + country)

#   my_function("Sweden")
#   my_function("India")
#   my_function()
#   my_function("Brazil")

# and more...