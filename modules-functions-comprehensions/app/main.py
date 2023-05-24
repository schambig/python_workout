import utils


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

def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)
  print(result)

if __name__ == '__main__':
  run()

# More info about if __name__ == '__main__':
# FreeCodeCamp: https://www.freecodecamp.org/news/if-name-main-python-example/
# Real Python: https://realpython.com/if-name-main-python/