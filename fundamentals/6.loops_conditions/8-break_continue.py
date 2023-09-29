'''
`break` and `continue` are control flow statements that are used in loops
(such as for and while) to modify the flow of execution.

The `break` statement is used to exit a loop prematurely. When encountered,
it immediately terminates the loop, and control is transferred to the next statement
following the loop.
It is often used to exit a loop based on a certain condition,
allowing you to break out of the loop before it would normally end.

The `continue` statement is used to skip the rest of the code inside a loop
for the current iteration and jump to the next iteration.
It is often used to avoid executing certain code for a particular iteration
while still continuing with the next iteration of the loop.
'''

# while loop runs indefinitely, printing values of count until count becomes greater
# than or equal to 5. The break statement is used to exit the loop when the condition is met.
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# The continue statement is used to skip the print(num) statement for even numbers.
# As a result, only odd numbers will be printed.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
