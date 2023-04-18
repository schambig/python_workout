# Using HOF with Regular Functions
def increment(x):
  return x + 1
def high_ord_func(x, func):
  return x + func(x)

res = high_ord_func(3, increment)
# 3 + (3 + 1)
print(res)

# Using HOF with Lambda Functions
increment_v2 = lambda x: x +1
high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func_v2(2, increment_v2)
print(result)

# We can just pass a lambda function as argument
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)


# In Python, a higher-order function (HOF) is a function that takes one or more functions as arguments, or returns a function as its result.
# Higher-order functions are often used to make code more reusable and concise.

# Some examples of higher-order functions in Python include:

#     map(): This function takes a function and an iterable as arguments,
#            and returns a new iterable that contains the results of applying the function to each element of the original iterable.
#     filter(): This function takes a function and an iterable as arguments,
#               and returns a new iterable that contains only the elements of the original iterable for which the function returns True.
#     reduce(): This function takes a function and an iterable as arguments,
#               and returns a single value that is the result of repeatedly applying the function to the elements of the iterable, starting with an initial value.
