'''
`for` statement is used to iterate over a sequence
(such as a list, tuple, string, or other iterable objects) or other iterable elements.
The general syntax of a for loop is as follows:
    for variable in iterable:
        # Code to be executed for each element in the iterable
        # This code block will be repeated for each element in the iterable
'''

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print()

'''
`for` loops are particularly useful when you know the number of iterations in advance
or when you want to iterate over the elements of a sequence. I
 you need to iterate over a sequence of numbers, you can use the range() function:
'''

for i in range(1, 6):  # Range from 1 to 5 (excluding 6)
    print(i)
