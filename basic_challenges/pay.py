#!/usr/bin/python3

class Pay:
    def __init__(self):
        pass


    def make_pay(self, quantity):
        return {
            'realized': True,
            'quantity': quantity,  # use the parameter passed to the method, not self.quantity
        }                          # bacause there's no such attribute defined in the Pay class
