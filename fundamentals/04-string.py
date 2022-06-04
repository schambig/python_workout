name = "Salomon"
last_name = 'Chambi Gutierrez'
print(name)
print(last_name)

# concatenacion con "+"
full_name = name + " " + last_name
print(full_name)

# single quote inside double quotes
quote = "I'm Nicolas"
print(quote)

# double quote inside single quotes
quote2 = ' She said "Hello"  '
print(quote2)

# Usando formatos con strings

# usando concatenacion y variables
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('concatenacion:', template)

# usando sintaxis punto con funcion format() and "{}"
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('funcion .format():', template)

# usando sintaxis f-strings y comillas dobles
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('f-strings:', template)