# Using Regular Functions
def increment(x):
  return x + 1
def high_ord_func(x, func):
  return x + func(x)

res = high_ord_func(3, increment)
# 3 + (3 + 1)
print(res)

# Using Higher Order Functions
increment_v2 = lambda x: x +1
high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func_v2(2, increment_v2)
print(result)

# We can jus pass a lambda function as argument
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)
