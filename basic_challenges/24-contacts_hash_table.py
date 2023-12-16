#!/usr/bin/python3

class ContactList:
    def __init__(self, size):
        self.size = size
        # This list will be used to store contacts, and the idea is to distribute contacts
        # across these sublists based on their hash values.
        self.contacts_list = [[] for _ in range(self.size)]


    # hash() function is a built-in function that returns the hash value of an object.
    def hash(self, key):
        # The modulo operator (%) is used to ensure that the index falls within
        # the range [0, size-1]
        return hash(key) % self.size


    def insert(self, name, phone):
        index = self.hash(name)
        # print(index)
        self.contacts_list[index].append((name, phone))


conts_list = ContactList(5)
print(conts_list.size)
print(conts_list.contacts_list)


print(conts_list.hash('Test'))


conts_list.insert('Mrs Pequeña', '666-555-444')
print(conts_list.contacts_list)
