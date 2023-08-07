'''
We can use input() function to get info/data from the user (stdin)
'''

full_name = input('What is your full name: ') # str by default

age = int(input('How old are you: ')) # casting to integer

height = float(input('How tall are you (in meters): ')) # casting to float

authorization = input('¿Do you authorize this program? (yes/no)') == 'yes'

print(full_name)
print(age)
print(height)
print(authorization)
