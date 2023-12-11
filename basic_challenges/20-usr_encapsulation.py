#!/usr/bin/python3

class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._friends = []
        self._messages = []


# # Accessing the private variable using name mangling
usr = User('Harvey', 30)
print(usr._User__name)
print(usr._User__age)
