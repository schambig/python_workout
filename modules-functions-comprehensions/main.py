# Import pkg # import everything from package pkg
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4


print(func_1())
print(func_2())
print(func_3())
print(func_4())

# Import pkg to access URL variable created in __init__.py
import pkg
print(pkg.URL)