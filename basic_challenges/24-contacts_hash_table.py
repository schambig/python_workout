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

    '''
    The insert method takes a name and phone as parameters.
    It calculates the index for the contact using the hash method.
    It then appends a tuple (name, phone) to the sublist at the computed index in
    the contacts_list.
    This means that contacts with similar hash values will be stored in the same sublist,
    providing a basic form of hash-based organization.
    '''
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
