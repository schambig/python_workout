'''
We can create sublists using the slicing funtionality in Python
syntax => list[start(inclusive):(stop)exclusive:step]
[star:] -> We get the last elements of the list
[:stop] -> We get the first elements of the list

start, stop and step are optional values we can use them as we need
'''

#               0           1       2           3       4     5                  
course_list = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
print(course_list)

sub_list = course_list[0:3]
print(sub_list)

# Invert the list order
sub_list = course_list[::-1]
print(sub_list)
