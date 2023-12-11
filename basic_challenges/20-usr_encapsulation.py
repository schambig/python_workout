#!/usr/bin/python3

class User:
    def __init__(self, name, age):
        # self.__name = name
        # self.__age = age
        self._name = name
        self._age = age
        self._friends = []
        self._messages = []

    
    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, new_name):
        self._name = new_name


    @property
    def age(self):
        return self._age
    

    @age.setter
    def age(self, new_age):
        self._age = new_age
    

    def addFriend(self, friend):
        self._friends.append(friend)

    
    def sendMessage(self, message, friend):
        self._messages.append(message)
        friend._messages.append(message)

    
    def showMessages(self):
        return self._messages

    
    def getFriends(self):
        return [(fren._name, fren._age) for fren in self._friends]


# # Accessing the private variable using name mangling, use this when you are trying to access
# # a private variable like variables at the beggining if the __init__ method
# usr = User('Harvey', 30)
# print(usr._User__name)  # Harvey
# print(usr._User__age)  # 30


usr1 = User('Mike', 28)
usr2 = User('Louis', 45)

usr1.addFriend(usr2)
print(usr1.getFriends())  # [('Louis', 45)]

usr1.sendMessage('Whatup fool', usr2)
print(usr1.showMessages())  # ['Whatup fool']


usr3 = User('Mike', 28)
usr3.name = 'Michael'
print(usr3.name)  # Michael
usr1.addFriend(usr3)
print(usr1.getFriends())  # [('Louis', 45), ('Michael', 28)]
