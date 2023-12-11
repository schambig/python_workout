#!/usr/bin/python3

class User:
    def __init__(self, name, age):
        self.__name = name  # private variable, use __
        self.__age = age  # private variable
        self._friends = []  # protected variable, use _
        self._messages = []  # protected variable


# # Accessing the private variable using name mangling
usr = User('Harvey', 30)
print(usr._User__name)  # Harvey
print(usr._User__age)  # 30
