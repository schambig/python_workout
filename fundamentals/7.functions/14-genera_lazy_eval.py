'''
 Lazy evaluation refers to the strategy of delaying the evaluation or computation
 of an expression until its value is actually needed.
 In the case of generators in Python, values are generated on-the-fly and only when requested,
 which aligns with the concept of lazy evaluation.

The examples below refer to Lazy Evaluation in the context of Generator
Because there's a more general concept of Lazy Evaluation:
  Lazy evaluation is a programming paradigm where the evaluation of an expression
  is delayed until its value is actually needed.
  This can lead to more efficient resource usage,
  especially when dealing with large datasets or complex computations.
 '''

def lazy_squared_generator(numbers):
    for num in numbers:
        yield num ** 2

numbers = [1, 2, 3, 4, 5]

# Creating a generator with lazy evaluation
squared_numbers_generator = lazy_squared_generator(numbers)

# No computation has happened yet

# Now, when we iterate over the generator, the squaring is performed on-the-fly
for squared_num in squared_numbers_generator:
    print(squared_num)  # print the square of each number in numbers list


# Another example of generator usgin try-except to handle the StopIteration error.
def even():
    for num in range(0, 10, 2):
        yield num  # Function execution is paused
        print('Function execution continues')

even_generator = even()  # create a generator with lazy evaluation

while True:
    try:
        even = next(even_generator)
        print(even)
    except StopIteration:
        print('Generator has finished')
        break
# Output:
# 0
# Function execution continues
# 2
# Function execution continues
# 4
# Function execution continues
# 6
# Function execution continues
# 8
# Function execution continues
# Generator has finished
