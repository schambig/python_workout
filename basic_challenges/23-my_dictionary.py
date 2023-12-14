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
        first_item = self.data[0]
        for item in range(1, self.length):
            self.data[item - 1] = self.data[item]
        del self.data[self.length -1]
        self.length -= 1
        return first_item


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
