price = 100 # global scope
# result = 200

def increment():
  price = 200 # local scope (this is not related with line 1)
  result = price + 10 # result variable is also of local scope
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
# print(result) # This is referencing line 2 (NOT line 6)

# More about scope in python
# https://www.w3schools.com/python/python_scope.asp

# global keyword: If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
# Also, use the global keyword if you want to make a change to a global variable inside a function.

# YT video on Scope
# https://www.youtube.com/watch?v=nKefMgHBNh0