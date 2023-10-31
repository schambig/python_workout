#!/usr/bin/python3

def get_student_average(students):
  averages = [
    round(sum(s['grades']) / len(s['grades']), 2)
    for s in students
  ]

  average = round(sum(averages) / len(averages), 2)
  names = [s['name'] for s in students]
  names_averages = [
    {'name': name, 'average': grade}
    for name, grade in zip(names, averages)
  ]

  return {
    'class_average': average,
    'students': names_averages,
  }

# print(get_student_average([
#   {
#     "name": "Pedro",
#     "grades": [90, 87, 88, 90],
#   },
#   {
#     "name": "Jose",
#     "grades": [99, 71, 88, 96],
#   },
#   {
#     "name": "Maria",
#     "grades": [92, 81, 80, 96],
#   },
# ]))
