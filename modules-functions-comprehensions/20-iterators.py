# Iterate using a for loop
for i in range(1, 10):
  print(i)

# Iterate manually using iter() and next() methods
my_iter = iter(range(1, 4))
print(my_iter) # <range_iterator object at 0x7f79fa63a1b0>
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) # Traceback (most recent call last):
#                          File "/home/salomon/githubRepos/python_workout/modules-functions-comprehensions/20-iterators.py", line 11, in <module>
#                            print(next(my_iter))
#                        StopIteration

# More about Python Iterators:
# https://www.w3schools.com/python/python_iterators.asp