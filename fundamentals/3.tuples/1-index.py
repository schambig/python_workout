'''
Remember Tuples are zero indexed!
We can access tuple elements by their indexes
We can use slicing with tuples
'''

courses = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#               0       1       2           3       4

first_course = courses[0]
print(first_course)

last_course = courses[-1]
print(last_course)

# Using slicing
sub_tuple = courses[:3]
print(sub_tuple)
