#!/usr/bin/python3
from pprint import pprint


class MyDict:
    def __init__(self):
        self.data = {}
        self.length = 0


    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    

    def shift(self):
        # Store the first item in a variable
        first_item = self.data[0]
        # Shift all elements one position to the left
        for item in range(1, self.length):
            self.data[item - 1] = self.data[item]
        # Delete the last element (which is now a duplicate of the second-to-last element)
        # "second-to-last element" refers to the element one position before the last element.
        del self.data[self.length -1]
        # Update the length of the list
        self.length -= 1
        return first_item
    

    def unshift(self, item):
        for i in range(self.length, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = item
        self.length += 1


dic = MyDict()
dic.append('S')
dic.append('a')
dic.append('l')
dic.append('o')
pprint(dic.data)  # {0: 'S', 1: 'a', 2: 'l', 3: 'o'}
pprint(dic.length)  # 4

dic.pop()
pprint(dic.data)  # {0: 'S', 1: 'a', 2: 'l'}
pprint(dic.length)  # 3

dic.shift()
pprint(dic.data)  # {0: 'a', 1: 'l'}

dic.unshift('Test')
pprint(dic.data)  # {0: 'Chambi', 1: 'a', 2: 'l'}
