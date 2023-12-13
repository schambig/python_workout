#!/usr/bin/python3
from pprint import pprint
from paypal import PayPal
from card import Card
from cash import Cash


'''
This module works in conjunction with `pay.py`, `paypal.py`, `card.py` modules
'''


def process_pay(payment_method, amount):
    return payment_method.make_pay(amount)


paypal = PayPal('email@example.com')
pprint(process_pay(paypal, 404))


card = Card('4444333322221111')
pprint(process_pay(card, 500))


cash = Cash()
pprint(process_pay(cash, 202))
