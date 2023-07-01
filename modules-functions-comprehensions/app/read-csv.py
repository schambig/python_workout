import csv


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
  print(data[162]) # Peru
  # for country in data:
  #   if country['Country/Territory'] == 'Peru':
  #     print(country)