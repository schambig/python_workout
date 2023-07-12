import sys


colecciones = {
    # mutables
    "list": list(),
    "dict": dict(),
    "set": set(),
    # mutables
    "tuple": tuple(),
    }

for name, value in colecciones.items():
    print(f'{name} = {sys.getsizeof(value)} bytes')