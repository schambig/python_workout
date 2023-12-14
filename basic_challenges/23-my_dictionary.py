#!/usr/bin/python3
from pprint import pprint


class MyDict:
    def __init__(self):
        self.data = {}
        self.length = 0


    def append(self, item):
        self.data[self.length] = item
        self.length += 1


dic = MyDict()
dic.append('S')
dic.append('a')
dic.append('l')
dic.append('o')
pprint(dic.data)  # {0: 'S', 1: 'a', 2: 'l', 3: 'o'}
pprint(dic.length)  # 4
