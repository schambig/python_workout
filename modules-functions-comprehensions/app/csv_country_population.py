import csv
import re
import utils

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      # country_dict = dict(iterable) # Does the same as line above
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/world_population.csv')
  # print(data[162]) # Peru

  # Print the whole dictionary
  for country in data:
    if country['Country/Territory'] == 'Peru':
      # popu_dic = {key[:-11]: int(value) for key, value in country.items() if re.match('^[0-9]', key)}
      keys, values = utils.get_year_popu_from_csv(country)
      print(keys, values)

  # Print the key: value pair formatted
  # for key, value in data[162].items():
    # print(key, value)
    # print(f"{key}: {value}")
    # print("{}: {}".format(key, value))