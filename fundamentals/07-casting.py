name = "Salomon"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

# Aqui estamos concatenando, pues son strings
print("Salomon" + " Chambi")
# Aqui estamos sumando, pues son numeros
print(10 + 20)

# print("Salomon" + 12) -> Output: Traceback... TypeError: can only concatenate str...
print("Salomon" + "12")

age = 12
print("Mi edad es " + str(age)) # Casteando age para que se peuda concatenar
print(f"Mi edad es {age}") # Usando f-strings para evitar castear, ya lo hace automaticamente

age = input('Escribe tu edad => ') # la funcion input siempre devuelve un string
print(type(age))
age = int(age)
# Tambien podemos usar input y castear al mismo tiempo: age = int(input('Escribe tu edad => '))
age += 10
print(f'Tu edad en 10 años sera: {age}')