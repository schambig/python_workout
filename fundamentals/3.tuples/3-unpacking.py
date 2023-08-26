'''
Tuple unpacking in Python is a convenient way to assign the elements of a tuple
to multiple variables in a single line of code.
It allows you to extract values from a tuple and assign them
to individual variables in one step.
'''

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

'''
If we add a new elements in nums that are not unpacked we got an error
    nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    one, two, three, four, five =  nums

But we can solve this issue using * operator
In Python, the * operator can be used for extended unpacking.
It allows you to collect multiple items into a single variable
or to unpack items from an iterable:
    one, two, three, four, *tuple_remainder =  nums
* character will let us to take the rest of the tuple into one variable

* -> makes reference to a list
_ -> omit values/variables

Using unpacking we can do it in one line
Instead of doing it variable by variable
    one = nums[0]
    two = nums[1]
    three = nums[2]
    four = nums[3]
    five = nums[4]
'''
one, two, three, four, *tuple_remainder =  nums
# one, two, three, four, *_ = nums              ---> To ommit the rest of the tuple elements
# one, two, three, four, *_, nueve, diez = nums ---> This will omit [5, 6, 7, 8]
# one, _, three, four, *_, nueve, diez = nums   ---> This will omit 2 and [5, 6, 7, 8]

print(one)
print(two)
print(three)
print(four)
print(tuple_remainder)

'''
While the term "unpacking" is commonly associated with tuples,
it is also applicable to other data types and structures in Python,
including lists, strings, and dictionaries.
'''

# List unpacking
numbers = [1, 2, 3]
a, b, c = numbers

print("a:", a)
print("b:", b)
print("c:", c)

# String unpacking
text = "abc"
x, y, z = text

print("x:", x)
print("y:", y)
print("z:", z)

# Dictionary unpacking
person = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
name, age, city = person.values()

print("Name:", name)
print("Age:", age)
print("City:", city)
