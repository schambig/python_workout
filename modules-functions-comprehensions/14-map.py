# Using the regular approach
numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

# Using map and lambda function (one liner)
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

# More about amp function:
# https://www.w3schools.com/python/ref_func_map.asp


# The map() function in Python is a higher-order function that takes a function and an iterable as arguments,
# and returns a new iterable that contains the results of applying the function to each element of the original iterable.

# For example, the following code uses the map() function to double the numbers in a list:

#     def double(x):
#       return 2 * x

#     numbers = [1, 2, 3, 4, 5]

#     doubled_numbers = list(map(double, numbers)) # if no cast output is => <map object at 0x7f138f44f6d0>

#     print(doubled_numbers) # [2, 4, 6, 8, 10]