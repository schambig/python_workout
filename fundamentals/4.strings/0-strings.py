'''
Inmmutable data type! meaning their values cannot be changed after they are created.
If you want to modify a string, you create a new one.
Strings use indexing and slicing.
Some of the most common string methods are:
    upper(), lower(), find(), replace(), split(), and join()
String formatting:
    format()
    f-strings
'''

# Create a list from a string using split() method
laguanges = 'Python Ruby Java Rust C++ C'
laguanges2 = 'Python-Ruby-Java-Rust-C++-C'

list_languages = laguanges.split() # use spaces by default
# list_languages2 = laguanges2.split('-') # use - to divide, given - is used in the string
list_languages2 = laguanges2.split('-', 2)  # we can indicate the separations we need (2 in this case)
                                            # the rest will be one element

print(list_languages) # ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']
print(list_languages2) # ['Python', 'Ruby', 'Java-Rust-C++-C']


# Create a string from a list usign join() method (opposite from split() method)
levels = ['Fundamental', 'Intermediate', 'Advanced', 'Asian']

string_levels = '@@'.join(levels) # we can use any character we need
print(string_levels) # Fundamental@@Intermediate@@Advanced@@Asian
print(type(string_levels)) # str
