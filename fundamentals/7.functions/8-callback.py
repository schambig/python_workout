'''
A callback refers to a function that is passed as an argument to another function
and is intended to be executed at a later time.
Essentially, a callback is a way to achieve a form of asynchronous programming
or to customize the behavior of a function.

Callbacks are commonly used in various scenarios, including:
    Event Handling: Callbacks are often used in event-driven programming,
                    where functions are triggered in response to specific events
                    (e.g., button click, mouse movement).
    Asynchronous Programming: In asynchronous programming, callbacks are used to handle
                              the completion of asynchronous tasks or operations.
    Customizing Behavior: Callbacks allow users to customize or extend the behavior of
                          a function without modifying its source code.
    Higher-Order Functions: Functions that take other functions as arguments,
                            such as those used in functional programming paradigms,
                            often involve the use of callbacks.
'''

# Simple example:
def perform_operation(x, y, callback):
    result = x + y
    callback(result)

# Define a callback function
def callback_function(result):
    print(f"The result is: {result}")

# Use the perform_operation function with the callback
perform_operation(2.3, 3.3, callback_function) # The result is: 5.6

# Second simple example:
average = lambda *args: sum(args) / len(args) # use lambda cos this isn't a complicated ope
passing_grade = lambda grade: grade >= 7

def show_message(func_average, func_passing_grade, *args):
    average = func_average(*args) # use * otherwise you will pass a tuple
    if func_passing_grade(average):
        print(f'Congratulations you passed with {average}')
    else:
        print('You didn\'t pass')

show_message(average, passing_grade, 10, 10, 8, 7, 5)
