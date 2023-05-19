import utils

keys, values = utils.get_population()
print(keys, values)

data = [
  {
    'Country': 'Peru',
    'Population': 500
  },
  {
    'Country': 'Colombia',
    'Population': 300
  }
]

country = input('Type Country => ')

result = utils.population_by_country(data, country)
print(result)