'''
This is `20-create-iterator.py`:
which would continue forever if you had enough next() statements, or if it was used in a for loop.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4
print(next(myiter)) # 5

To prevent the iteration from going on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# More about Python Iterators:
# https://www.w3schools.com/python/python_iterators.asp