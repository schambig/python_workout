'''
Instance attributes in Python are variables that belong to an instance of a class.
Unlike class attributes, which are shared among all instances of a class,
instance attributes are unique to each instance.
They are defined within the methods of the class, typically in the __init__ method,
and they store data that varies from one instance to another.
'''

# Let's consider a Person class with instance attributes that represent personal information
# such as name, age, and address.
# The class may also have methods to perform actions related to the person,
# such as updating their address. Here's a simple implementation:
class Person:
    def __init__(self, name, age, address):
        # Instance attributes
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

    def update_address(self, new_address):
        print(f"Updating address for {self.name} from {self.address} to {new_address}.")
        self.address = new_address

# Creating instances of the Person class
person1 = Person(name="Alice", age=30, address="123 Main St")
person2 = Person(name="Bob", age=25, address="456 Oak Ave")

# Displaying information about each person
person1.display_info()  # Name: Alice, Age: 30, Address: 123 Main St
person2.display_info()  # Name: Bob, Age: 25, Address: 456 Oak Ave

# Updating the address for person1
person1.update_address(new_address="789 Elm St")  # Updating address for Alice from 123 Main St to 789 Elm St.

# Displaying updated information
person1.display_info()  # Name: Alice, Age: 30, Address: 789 Elm St
person2.display_info()  # Name: Bob, Age: 25, Address: 456 Oak Ave

'''
The __dict__ attribute is a dictionary that contains the namespace of an instance or a class.
  - For instances, it holds the instance attributes and their values,
    allowing you to access and manipulate them dynamically.
  - For classes, it holds the class attributes and methods, The keys of the dictionary
    are the attribute or method names, and the values are the corresponding objects or functions.
'''

# Accessing instance namespace using __dict__
print(person1.__dict__)  # 'name': 'Alice', 'age': 30, 'address': '789 Elm St'}

# Modifying an instance attribute using __dict__
# NOTE THAT THIS KIND OF MODIFICATION IS NOT RECOMMENDED
person1.__dict__['age'] = 99

# Accessing the modified instance attribute
print(person1.age)  # 99


# Accessing the class namespace using __dict__
print(Person.__dict__)
# Output:
# {'__module__': '__main__', '__init__': <function Person.__init__ at 0x7f0ad32c2d30>,
#  'display_info': <function Person.display_info at 0x7f0ad32d0040>,
#  'update_address': <function Person.update_address at 0x7f0ad32d00d0>, ...}
