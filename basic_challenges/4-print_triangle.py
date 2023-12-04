#!/usr/bin/python3

# Using a variable to return the triangle
def print_triangle(size, char):
    tri = ''
    for s in range(size):
        tri += ' ' * (size - s - 1)
        tri += char * (2 * s + 1)
        if s < size:
            tri += '\n'
    return tri

print(print_triangle(1, '#'))
print(print_triangle(2, '$'))
print(print_triangle(3, '@'))
print(print_triangle(7, '&'))
print(print_triangle(10, '?'))


# Directly printing
def print_triangle2(size, char):
    for s in range(size):
        print(' ' * (size - s - 1) + char * (2 * s + 1))

print_triangle2(1, '#')
print_triangle2(2, '$')
print_triangle2(3, '@')
print_triangle2(7, '&')
print_triangle2(10, '?')
