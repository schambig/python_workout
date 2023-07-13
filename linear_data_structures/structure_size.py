import sys


colecciones = {
    # mutables
    "list": list(),
    "dict": dict(),
    "set": set(),
    # immutables
    "tuple": tuple(),
    }

for name, value in colecciones.items():
    print(f'{name} = {sys.getsizeof(value)} bytes')
