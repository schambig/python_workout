#!/usr/bin/python3
from mail import Mail


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
