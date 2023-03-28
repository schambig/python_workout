def sum_with_range(min, max):
  print(f"Suma desde {min} hasta {max - 1}:")
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result) # 45
result_2 = sum_with_range(result, result + 10)
print(result_2) # 495

# More info about function return:
# https://www.w3schools.com/python/python_functions.asp

# Return Values
#   def my_function(x):
#     return 5 * x

#   print(my_function(3))
#   print(my_function(5))
#   print(my_function(9))

