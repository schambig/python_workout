# Una lista de listas
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1]) # Output: 2 
print()

# for element in matriz:
#   print(element)
#   for item in element:
#     print(item)

for row in matriz:
  print(row)
  for column in row:
    print(column)
  # Output: 
  # [1, 2, 3]
  # 1
  # 2
  # 3
  # [4, 5, 6]
  # 4
  # 5
  # 6
  # [7, 8, 9]
  # 7
  # 8
  # 9