#!/usr/bin/python3

class Product:
    '''This Class is used by 19-shopping_cart.py module'''
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def addToCart(self):
        raise NotImplementedError("This method will be overriden by the children classes")
