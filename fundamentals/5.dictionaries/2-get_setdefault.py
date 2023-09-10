'''
get() method is used to retrieve the value associated with a specified key
It takes two arguments: the key to look up, and an optional default value to return
if the key is not found.
If the key is present in the dictionary, get() returns the corresponding value;
otherwise, it returns the default value or None if no default is specified.

setdefault() method is used to insert a key-value pair if the specified key doesn't exist.
If the key is already present, it returns the corresponding value without modifying the dict.
'''

# get() is useful when you want to retrieve a value but also
# handle the case where the key might not exist in the dictionary.
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Using get() to retrieve values
name = my_dict.get("name")
print(name) # John

# Specifying a default value
gender = my_dict.get("gender", "Not specified")
print(gender) # Not specified

# setdefault() method is handy when you want to add a default value for a key
# only if the key is not already present in the dictionary.
# It helps avoid overwriting existing values.
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Using setdefault() to insert a new key-value pair
country = my_dict.setdefault("country", "USA")
print(my_dict)
# {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Using setdefault() on an existing key
age = my_dict.setdefault("age", 30)
print(age) # 25 (value is not modified)

'''
In summary, get() is primarily used for retrieving values with the option
to provide a default if the key is not found,
while setdefault() is used for safely inserting a new key-value pair
into the dictionary if the key does not already exist.
'''
