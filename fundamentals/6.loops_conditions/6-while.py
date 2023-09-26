'''
`while` is a control flow statement that allows you to repeatedly execute a block of code
as long as a specified condition is true.
The general syntax of a while loop is as follows:
    while (condition):
        # Code to be executed while the condition is true
        # This code block will be repeated until the condition becomes false
'''

# while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Get the number of digits in a number using a wile loop and dividing by 10
number = 1234567890
counter = 0
while number >= 1:
    counter += 1
    number /= 10
else: # use else keyword to execute another block of code when needed
    print(counter) 
