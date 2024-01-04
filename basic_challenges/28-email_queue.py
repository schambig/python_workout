#!/usr/bin/python3
from mail import Mail
from pprint import pprint


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
        if self.length == 0:
            raise IndexError('The queue is empty.')
        if self.first == self.last:
            self.last = None
        removed_node = self.first
        self.first = self.first.next
        self.length -= 1
        # return removed_node.__dict__
        return {
            'from': removed_node.from_email,
            'to': removed_node.to,
            'body': removed_node.body,
            'subject': removed_node.subject
        }


    def peek(self):
        if self.length == 0:
            raise IndexError('The queue is empty.')
        else:
            return {
                'from': self.first.from_email,
                'to': self.first.to,
                'body': self.first.body,
                'subject': self.first.subject
            }        


    def is_empty(self):
        return self.length == 0


    def size(self):
        return self.length


email_queue = Queue()
email_queue.enqueue(
    'salo@example.me',
    'support@company.com',
    'I can\'t access my account',
    'Signing in issue'
)
email_queue.enqueue(
    'luis@example.me',
    'support@company.com',
    'I found a bug in your system',
    'Don\'t ignore this message!'
)
pprint(email_queue.__dict__)
# Output
# {'first': <mail.Mail object at 0x7fcc2a0acc10>,
#  'last': <mail.Mail object at 0x7fcc2a0acc10>,
#  'length': 1}

email = email_queue.dequeue()
pprint(email)
# Output using line `return removed_node.__dict__`
#   {'body': "I can't access my account",
#    'from_email': 'salo@example.me',
#    'next': None,
#    'subject': 'Signing in issue',
#    'to': 'support@company.com'}
# Output using line `return {...}`
#     {'body': "I can't access my account",
#      'from': 'salo@example.me',
#      'subject': 'Signinig in issue',
#      'to': 'support@company.com'}

# email = email_queue.dequeue()
# pprint(email)
# # Output
# # IndexError: The queue is empty.

pprint(email_queue.peek())
# Output
# {'body': 'I found a bug in your system',
#  'from': 'luis@example.me',
#  'subject': "Don't ignore this message!",
#  'to': 'support@company.com'}

pprint(email_queue.is_empty())  # Output: False

pprint(email_queue.length)  # Output: 1
