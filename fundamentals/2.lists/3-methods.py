'''
append('element') method lets us to add new elements at the end of the list.
insert(index, 'element') method lets us to add new elements at a given index
We can add any type of data 
extend() method lets us to join/merge two lists
remove() method lets us to remove an element by its name
`del` keyword lets us to delete an element by its index
clear() method lets us to delete/remove all the elements in a list
'''

course_list = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
print(course_list)
print(len(course_list))

course_list2 = ['C', 'C#', 'Docker']

# Using append() method
course_list.append('MongoDB')
course_list.append('ThreeJS')

print(course_list)
print(len(course_list))

# Using insert() method and a given index
course_list.insert(1, 'C++')
course_list.insert(len(course_list), 'TypeScript') # inserting at the end

print(course_list)
print(len(course_list))

# 'Merging' two list
course_list.extend(course_list2)
print(course_list)
print(len(course_list))

# Deleting/removing list elements unsing remove('element') method
course_list.remove('Docker')
print(course_list)
print(len(course_list))

# Deleting/removing elements using del keyword and an index
del course_list[0]
print(course_list)
print(len(course_list))

# Deleting/removing all the list elements
course_list.clear()
print(course_list)
print(len(course_list))
