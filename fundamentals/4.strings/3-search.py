'''
Finding strings within strings using:
count('elem') method which let us know the number of coincidences of `elem` in a string.
`in` and `not in` keywords let us know whether a string is or is not within a string.
startswith() and endswith() let us know is a certain string is at the beginning or the end.
'''

course = 'We are learning Python language and using Python methods, data types, etc'

counter = course.count('Python')
print(counter) # 2

# Using `in` keyword to search a string within a string
print('Python' in course) # True
print('python' in course) # False, because Python is case sensitive

# We can 'normalize' a string to all lawercase or uppercase using lower() and upper() methods
print('python' in course.lower()) # True
print('salomon' not in course.lower()) # True

# Using startswith() and endswith() methods
print(course.startswith('We')) # True
print(course.endswith(', etc')) # True
