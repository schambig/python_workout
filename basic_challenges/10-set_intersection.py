#!/usr/bin/python3

def find_set_intersection(sets):
  inte = set()
  for s in range(len(sets)):
    if s == 0:
      inte = sets[0]
    inte = inte.intersection(sets[s])
  return inte

# Using slicing within a loop
def find_set_intersection2(sets):
  inte = sets[0] if sets else set()
  for s in sets[1:]:
    inte = inte.intersection(s)
  return inte

# Using *sets[1:] to unpack the list of sets and pass them as separate arguments to the intersection method.
def find_set_intersection3(sets):
    return sets[0].intersection(*sets[1:]) if sets else set()

print(find_set_intersection([
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]))

print(find_set_intersection([
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]))
