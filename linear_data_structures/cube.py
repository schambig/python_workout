from array_1 import Array


"""
Code used to 'Crear un array de tres dimensiones' class.

Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Get depth
    5. Access item
    6. String representation
"""
class Cube(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, cols, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols)
            for col in range(cols):
                    self.data[row][col] = Array(depth, fill_value)

    def get_height(self):
        """Returns the number of rows."""
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])
    
    def get_depth(self):
        """Returns the number of columns."""
        return len(self.data[0][0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + " "

                result += "\n"

        return str(result)

'''
Code used in the shell to instance a grid

cube = Cube(3, 3, 3)
print(cube)
for row in range(cube.get_height()):
    for column in range(cube.get_width()):
        for depth in range(cube.get_depth()):
            cube[row][column][depth] = row * column * depth

print(cube)
cube.get_height()
cube.get_width()
cube.get_depth()
cube.__getitem__()
cube.__getitem__(1)
cube.__getitem__(2)[0][0]
cube.__str__()
'''