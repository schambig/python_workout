import re


def get_year_popu_from_csv(data):
  year_popu = {key[:-11]: int(value) for key, value in data.items() if re.match('^[0-9]', key)}
  keys = year_popu.keys()
  values = year_popu.values()
  return keys, values 

def get_population():
  keys = ['per', 'col']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result