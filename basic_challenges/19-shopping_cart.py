#!/usr/bin/python3
from product import Product


''' This module works in conjunction with `product.py` module '''


class Article(Product):
    def addToCart(self):
        return f'Adding {self.quantity} units of the article {self.name} to the cart'
    

class Service(Product):
    def addToCart(self):
        return f'Adding service {self.name} to the cart' 


class Cart:
    def __init__(self):
        self.shopping_cart = []
    

    def addProduct(self, product):
        self.shopping_cart.append(product)
        return product.addToCart()


    def deleteProduct(self, product):
        self.shopping_cart.remove(product)
        return f'Deleting {product.name} from shopping cart'


    def caculateTotal(self):
        return sum((product.price * product.quantity) for product in self.shopping_cart)


    def getProducts(self):
        return [(product.name, product.price, product.quantity) \
                for product in self.shopping_cart]


book = Article('Book', 100, 2)
# print(book.addToCart())
course = Service('Course', 150, 1)
# print(course.addToCart())

cart = Cart()
print(cart.addProduct(book))
print(cart.addProduct(course))
print(cart.getProducts())
# print(cart.deleteProduct(book))
print(cart.deleteProduct(course))
# print(cart.getProducts())
print(cart.caculateTotal())
