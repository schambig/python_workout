import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2) # {'col': 14, 'mex': 59, 'bol': 63, 'pe': 95}

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result) # {'mex': 59, 'bol': 63, 'pe': 95}

text = 'Hola, soy Salomon Luis'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique) # {'o': 'O', 'a': 'A', 'u': 'U', 'i': 'I'}

texto = 'Hola, soy Salomon Luis'
dictio = { c: texto.count(c) for c in texto if c in 'aeiou' }
print(dictio) # {'o': 4, 'a': 2, 'u': 1, 'i': 1}