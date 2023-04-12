def increment(x):
  return x + 1

increment_v2 = lambda x: x + 1

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('salomon', 'chambi gutierrez')
print(text)

# Fibonacci series using lambda function and recursion:

# fibonacci = lambda x: 0 if x == 0 else 1 if x < 3 else fibonacci(x - 1) + fibonacci(x - 2)
# print(fibonacci(int(input('Enter a number: '))))

# More about Lamdba functions:
# https://www.w3schools.com/python/python_lambda.asp