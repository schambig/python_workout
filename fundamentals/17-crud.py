# CRUD Create, Read, Update & Delete

numbers = [1, 2 , 3 , 4 , 5]
print(numbers[1]) # Output: 2
numbers[-1] = 10
print(numbers) # Output: [1, 2, 3, 4, 10]

numbers.append(700)
print(numbers) # Output: [1, 2, 3, 4, 10, 700]

numbers.insert(0, 'hola')
print(numbers) # Output: ['hola', 1, 2, 3, 4, 10, 700]

numbers.insert(3, 'change')
print(numbers) # Output: ['hola', 1, 2, 'change', 3, 4, 10, 700]

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list) # Output: ['hola', 1, 2, 'change', 3, 4, 10, 700, 'todo 1', 'todo 2', 'todo 3']

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list) # Output: ['hola', 1, 2, 'change', 3, 4, 10, 700, 'todo 1', 'todo changed', 'todo 3']

new_list.remove('todo 1')
print(new_list) # Output: ['hola', 1, 2, 'change', 3, 4, 10, 700, 'todo changed', 'todo 3']

new_list.pop()
print(new_list) # Output: ['hola', 1, 2, 'change', 3, 4, 10, 700, 'todo changed']

new_list.pop(0)
print(new_list) # Output: [1, 2, 'change', 3, 4, 10, 700, 'todo changed']

new_list.reverse()
print(new_list) # Output: ['todo changed', 700, 10, 4, 3, 'change', 2, 1]

numbers_a = [1, 4, 6 , 3]
numbers_a.sort()
print(numbers_a) # Output: d', 700, 10, 4, 3, 'change', 2, 1]

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings) # Output: ['ab', 'ed', 're']

# new_list.sort() Output: TypeError: '<' not supported between instances of 'int' and 'str'