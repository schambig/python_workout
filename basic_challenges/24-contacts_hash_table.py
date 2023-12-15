#!/usr/bin/python3

class ContactList:
    def __init__(self, size):
        self.size = size
        self.contacts_list = [[] for _ in range(self.size)]

    
    # hash() function is a built-in function that returns the hash value of an object.
    def hash(self, key):
        return hash(key) % self.size


conts_list = ContactList(5)
print(conts_list.size)
print(conts_list.contacts_list)

print(conts_list.hash('Test'))
