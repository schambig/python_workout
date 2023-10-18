'''
A generator is a special type of iterable, similar to a list or a tuple.
However, unlike lists or tuples, generators do not store all the values in memory at once.
Instead, they generate values on the fly as you iterate over them.
This makes generators more memory-efficient, especially when dealing with large datasets.

Generators are created using functions with the `yield` statement.
When a generator function is called, it returns a generator object,
which can be iterated over to produce values.
The state of the generator function is saved between calls,
allowing it to resume from where it left off.
'''

# STANDARD Function that return even numbers using `return` keyword
def even():
    for num in range(0, 100, 2):
        # using `return` the function returns the first number `0` then stops
        # after the first iteration
        return num
        print('Not printed because `return` keyword')

print(even())  # 0

# GENERATOR Function that return even numbers using `yield` keyword
# `yield` let us return the object and then pause the function execution to start over again
# in the next iteration
def even2():  # Generator -> Lazy evaluation
    for num in range(0, 100, 2):
        yield num  # function pause its execution
        print('Printed because `yield` keyword')

print(even2())  # <generator object even2 at 0x7f2df9489ba0>
# Now let's iterate over our generator function in two ways
# List conprehension:
print([even for even in even2()])  # print a list of even numbers from 0 to 98
# For loop:
for even in even2():
    print(even)  # print every even number in its own line from 0 to 98


# Simple example
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for i in countdown(5):
    print(i)

'''
In this example, countdown is a generator function that yields values from n down to 1.
When the generator is iterated over in the for loop, it produces values one at a time,
and the state of the function is saved between each iteration.
'''

'''
Some key points about generators:
    Memory Efficiency: Generators are memory-efficient because they generate values on-the-fly
                       and don't store the entire sequence in memory.
    Lazy Evaluation: Values are generated as needed, making generators suitable for working
                     with large datasets or infinite sequences.
    Use of yield: The yield statement is used to produce a value from the generator function.
                  When yield is encountered, the function's state is frozen until
                  the next iteration.
    Iterability: Generators are iterable, so you can use them in for loops, list comprehensions,
                 and other iterable contexts.
'''

# Here's a simple example to illustrate lazy evaluation using a generator
# for an infinite sequence of Fibonacci numbers:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to generate the first 50 Fibonacci numbers
fibonacci_gen = fibonacci_generator()
first_fifty_fibonacci = [next(fibonacci_gen) for _ in range(50)]
print(first_fifty_fibonacci)  # print a list of the first 50 fibonacci nums

fibonacci_gen = fibonacci_generator()
# res = []
for _ in range(50):
    # val = next(fibonacci_gen)
    # res.append(val)
    print(next(fibonacci_gen))  # prints the first 50 fibonacci nums one in its own line
# print(res)
'''
In this example, the Fibonacci sequence is generated on-the-fly,
and you can consume as many values as needed without having to compute the entire sequence.
'''
