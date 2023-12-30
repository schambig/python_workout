#!/usr/bin/python3
from mail import Mail


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, from_email, to, body, subject):
        pass


    def dequeue(self):
        pass


    def peek(self):
        pass


    def is_empty(self):
        pass


    def size(self):
        pass
