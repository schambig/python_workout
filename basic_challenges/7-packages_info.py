#!/usr/bin/python3
from pprint import pprint

def get_packages_info(packs):
   # using a generator expression inside sum() function, it is not called tuple comprenhension
   total = round(sum(tup[1] for tup in packs), 2)
   countries = [tup[2] for tup in packs]
   dest = {c: countries.count(c) for c in countries}
   return {
      'total_weight': total,
      'destinations': dest,
   }

# It is suposed to use uderscore to indicate to not use that variable
# but it is not working here :(
def get_packages_info2(packs):
    total = round(sum(tup[1] for tup in packs), 2)
    # line below won't work becuase:
    #    1.For each unique country, the packs.count(c) counts the occurrences of that country
    #      in the entire list, not just the remaining items.
    #    2.As a result, when you move to the next country, the count is affected by
    #      the occurrences of the previous country.
    #    3.This leads to incorrect counts, especially when there are multiple occurrences of
    #      a country in the list.
    #   dest = {c: packs.count(c) for _, _, c in packs}
    dest = {country: sum(1 for _, _, c in packs if c == country) for _, _, country in packs}
    return {
       'total_weight': total,
       'destinations': dest,
    }


pprint(get_packages_info([
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]))
