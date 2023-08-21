'''
We can create a matrix using nested list (lists whitin lists)
Remember: lists are zero indexed
'''

col_a = [10, 20, 30, 40]
col_b = [30, 40, 50, 60]

matriz = [col_a, col_b] # 2 x 4

print(matriz[1][3])

# Create a 3D list (Cube)

# # Define the size of the cube (side length)
# side_length = 3

# # Create a 3D list to represent the cube
# cube = [[[0 for _ in range(side_length)] for _ in range(side_length)] for _ in range(side_length)]

# # Display the cube
# for layer in cube:
#     for row in layer:
#         print(row)
#     print()
