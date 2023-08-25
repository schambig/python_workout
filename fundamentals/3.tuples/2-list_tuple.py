'''
Use square brackets usually with lists []
Use parenthesis usally with tuples ()
'''

courses = ['Python', 'Flask', 'Django', 'Rails', 'MongoDB']

# Casting a list into a tuple
tuple_courses = tuple(courses)
print(tuple_courses)
print(type(tuple_courses))

levels = ('Fundamental', 'Intermediate', 'Advanced')

# Casting a tuple into a lisy
list_levels = list(levels)
print(list_levels)
print(type(list_levels))
