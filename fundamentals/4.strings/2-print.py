'''
Primary function for outputting values to the console.
Supports options like sep for separator and end for the end character.
Can redirect output to a file using the file parameter.
Supports escape sequences for special characters like newline and tab.

REMEMBER!! print() functions just prints to stdout
'''

name = 'Salomon'
name2 = 'Luis'

print(name, name2, 'Chambi', sep=' ') # we can use different chars as sep
print(name, name2, 'Chambi', sep='^', end='\n') # a jump line at the end

