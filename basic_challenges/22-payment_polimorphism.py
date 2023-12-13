#!/usr/bin/python3
from pprint import pprint
from paypal import PayPal


'''
This module works in conjunction with `pay.py`, `paypal.py` modules
'''


def process_pay(payment_method, amount):
    return payment_method.make_pay(amount)


paypal = PayPal('email@example.com')
pprint(process_pay(paypal, 404))
