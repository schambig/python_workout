#!/usr/bin/python3

def get_packages_info(packs):
   # using a generator expression inside sum() function, it is not called tuple comprenhension
   total = round(sum(tup[1] for tup in packs), 2)
   countries = [tup[2] for tup in packs]
   dest = {c: countries.count(c) for c in countries}
   return {
      'total_weight': total,
      'destinations': dest,
   }

# # It is suposed to use uderscore to indicate to not use that variable
# # but it is not working here :(
# def get_packages_info(packs):
#     total = round(sum(tup[1] for tup in packs), 2)
#     dest = {c: packs.count(c) for _, _, c in packs}
#     return {
#        'total_weight': total,
#        'destinations': dest,
#     }

# print(get_packages_info([
#   (1, 20, "Mexico"),
#   (2, 15.5, "Colombia"),
#   (3, 30, "Mexico"),
#   (4, 12, "Argentina"),
#   (5, 8.2, "Colombia"),
#   (6, 25, "Mexico"),
#   (7, 18.7, "Argentina"),
#   (8, 5, "Colombia"),
#   (9, 22.3, "Argentina"),
#   (10, 14.8, "Colombia")
# ]))
