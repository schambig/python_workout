# Tenemos una lista de estudiantes de la cual debemos saber quienes son de Peru y,
# quienes son considerados mayores de edad y cuantos son.
students = [
  {
    'name' : 'Pedro',
    'country': 'Peru',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Colombia',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Peru',
    'age' : 25,
    'course' : 'Tester'
  }
]

# Ahora planteamos el primer problema a resolver, cuales son los estudiantes de Peru y cuantos son:
per_stud = list(filter(lambda x: x['country'] == 'Peru', students))
print(per_stud)
print(len(per_stud)) # 2

# Ahora necesitamos saber quienes son considerados mayores de edad al tener 18 años o más:
legal = list(filter(lambda x: x['age'] >= 18, students))
print(legal)
print(len(legal)) # 3