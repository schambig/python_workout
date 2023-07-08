import utils
import charts
import csv_country_population


def run():
  data = csv_country_population.read_csv('./world_population.csv')
  country = input('Select country to graph 📊 => ')
  result = utils.population_by_country(data, country)
  print(result)

  if result: # This returns a list with a single dict, so we want to access it
    keys, values = utils.get_year_popu_from_csv(result[0])
    charts.generate_bar_chart(keys, values)
    charts.generate_pie_chart(keys, values)


if __name__ == '__main__':
  run()


# More info about if __name__ == '__main__':
# FreeCodeCamp: https://www.freecodecamp.org/news/if-name-main-python-example/
# Real Python: https://realpython.com/if-name-main-python/