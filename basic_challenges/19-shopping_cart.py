#!/usr.bin/python3
from product import Product


class Article(Product):
    def addToCart(self):
        return f'Adding {self.quantity} units of the article {self.name} to the cart'
    

class Service(Product):
    def addToCart(self):
        return f'Adding service {self.name} to the cart' 


book = Article('Book', 100, 2)
print(book.addToCart())
course = Service('Course', 150, 1)
print(course.addToCart())
