#!/usr/bin/python3
from pay import Pay


class Cash(Pay):
    def make_pay(self, quantity):
        return super().make_pay(quantity)
    # pass  # use pass keyword to return the same as Pay class
