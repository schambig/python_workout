'''
__init__ is a special method, also known as a constructor,
that is automatically called when an object is created from a class.
The __init__ method is used to initialize the attributes of the object with specified values.
'''

'''
Let's consider a Book class.
This class could be used to represent books in a library with attributes like
title, author, and ISBN (International Standard Book Number).
The __init__ method would be responsible for INITIALIZING these attributes when
a new book instance is created.
Here's an example:
'''

class Book:
    # `self` makes reference to the object (that will be instantiated) itself
    # Here we can say that we are 'overwriting' the __init__ method from the Object class
    # which is from all classes inherit from. 
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
        availability = "Available" if self.available else "Not Available"
        print(f"Status: {availability}")

    def borrow_book(self):
        if self.available:
            print(f"Borrowing {self.title} by {self.author}.")
            self.available = False
        else:
            print(f"Sorry, {self.title} is not available for borrowing.")

    def return_book(self):
        if not self.available:
            print(f"Returning {self.title} by {self.author}.")
            self.available = True
        else:
            print(f"{self.title} is already available in the library.")

# Creating instances of the Book class
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="978-0743273565")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="978-0061120084", available=False)
book3 = Book("1984", "George Orwell", isbn="978-0140817744")

# Displaying information about each book
book1.display_info()
# Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 978-0743273565
# Status: Available
book2.display_info()
# Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 978-0061120084
# Status: Not Available
book3.display_info()
# Title: 1984, Author: George Orwell, ISBN: 978-0140817744
# Status: Available

# Borrowing and returning books
book1.borrow_book()  # Borrowing The Great Gatsby by F. Scott Fitzgerald.
book2.borrow_book()  # Sorry, To Kill a Mockingbird is not available for borrowing.
book3.borrow_book()  # Borrowing 1984 by George Orwell.
book1.return_book()  # Returning The Great Gatsby by F. Scott Fitzgerald.
book2.return_book()  # Returning To Kill a Mockingbird by Harper Lee.
book3.return_book()  # Returning 1984 by George Orwell.

'''
In this example:
  - The Book class has attributes (title, author, isbn, and available) representing information
    about each book. The available attribute is a boolean indicating whether
    the book is currently available for borrowing.
  - The __init__ method initializes these attributes when a new book instance is created.
    The available attribute has a default value of True, assuming the book is available by default.
  - The `display_info` method prints out information about the book and its availability status.
  - The `borrow_book` and return_book methods simulate the process of borrowing and returning books,
    updating the available attribute accordingly.

    This example showcases how the __init__ method is used to set up the initial state
    of the book objects when they are created.
'''
