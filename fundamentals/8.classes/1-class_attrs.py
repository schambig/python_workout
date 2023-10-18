'''
Class attributes are attributes that are shared by all instances of a class.
They are defined at the class level and are the same for every instance of that class.
These attributes are typically used to store information that is common to all instances
of the class.
'''

# Creating class attributes
class User:
    username = 'default username'
    email = 'defaultemail@example.com'

# Updating class attributes
User.username = 'updated username'
User.email = 'updatedemail@example.com'

print(User.username)  # updated username
print(User.email)  # updatedemail@example.com
