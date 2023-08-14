'''
Python lists are zero indexed meaning the first element of the list in index = 0
We can access list elements using its indexes
'''

#               0           1       2           3       4                       
#               -5          -4      -3          -2      -1
course_list = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

print(course_list)  # Print original list
print(course_list[0])  # Print the fisrt element of the list 'Python'
print(course_list[1])  # Print the second element of the list 'Django'
print(course_list[-1])  # Print the last element of the list 'Java'

course_list[-1] = 'Rust'
print(course_list)  # Print list with the element in -1 index updated to 'Rust'
