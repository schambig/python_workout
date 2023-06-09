# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# All classes have a function called __init__(), which allows you to do some initializing when the object is being created.
#   The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#   The __next__() method also allows you to do operations, and must return the next item in the sequence.

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
