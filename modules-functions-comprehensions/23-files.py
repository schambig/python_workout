file = open('./zenpy.txt')
# print(file.read()) #
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

with open('./zenpy.txt') as file:
  for line in file:
    print(line)
