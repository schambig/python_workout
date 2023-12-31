#!/usr/bin/python3
from mail import Mail


''' This module works in conjunction with `mail.py` module '''


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0


    def enqueue(self, from_email, to, body, subject):
        new_node = Mail(from_email, to, body, subject)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


    def dequeue(self):
        pass


    def peek(self):
        pass


    def is_empty(self):
        pass


    def size(self):
        pass


email_queue = Queue()
email_queue.enqueue(
    'salo@example.me',
    'support@company.com',
    'I can\'t access my account',
    'Signinig in issue'
)
print(email_queue.__dict__)