<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/python_workout)

# Basic Python Challenges<!--@schambig-->


[Description](#description) • [File Structure](#file-structure)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code:

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.10)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-zen.py](0-zen.py)</pre><!--@schambig--> | `The Zen of Python` consists of nineteen aphorisms, some of which favor one specific trait over another, providing opinions about what makes your code better, you should print it to the standard output usgin just only 11 characters.<br> [More Python Easter Eggs](https://github.com/OrkoHunter/python-easter-eggs) |
```
Input: python3 0-zen.py

Output:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

| Filename | Description/Task |
| --- | --- |
| <pre>[1-value_type.py](1-value_type.py)</pre><!--@schambig--> | In this challenge, you will find a function called `found_type` that takes a parameter called `value`. Your task is to determine the data type of the value parameter and return it from the `found_type` function.|
```
Input:
found_type(1)
found_type("Salo")
found_type(True)

Output:
'int'
'str'
'bool'
```

| Filename | Description/Task |
| --- | --- |
| <pre>[2-caculate_tip.py](2-caculate_tip.py)</pre><!--@schambig--> | In this challenge, you will need to calculate the tip that restaurant customers should leave based on their bill. The `calculate_tip` function will receive two parameters: `bill_amount`, representing the total cost of what was consumed, and `tip_percentage`, representing the percentage of the tip to leave. Both values will be of type float and will always be positive, including 0. The function should return the tip amount as a number.|
```
Input: calculate_tip(100, 10)
Output: 10

Input: calculate_tip(1524.33, 25)
Output: 381.08
```

| Filename | Description/Task |
| --- | --- |
| <pre>[3-is_leap_year.py](3-is_leap_year.py)</pre><!--@schambig--> | In this Python challenge, you need to create the logic for the `is_leap_year` function, which determines whether a year is a leap year or not. A year is a leap year if it meets the following conditions:<br> • It is divisible by 4, but not by 100.<br> • If it is divisible by 100, it must also be divisible by 400.<br> The `is_leap_year` function takes a single parameter, which is the year to evaluate. It should return True if the year is a leap year or False if it is not. Keep in mind that the function should be able to handle non-integer or negative values. |
```
Input: is_leap_year(2000)
Output: True

Input: is_leap_year(-2024)
Output: False

Input: is_leap_year(1984.25)
Output: False
```

| Filename | Description/Task |
| --- | --- |
| <pre>[4-print_triangle.py](4-print_triangle.py)</pre><!--@schambig--> | In this challenge, you need to draw an triangle using loops. You will receive two parameters: `size` and `char`, which define the number of rows the triangle will have and the character with which the triangle should be constructed, respectively. Additionally, the triangle should be centered, which means the same number of characters should be on both sides. Remember that to create a line break, you should use "\n". Don't forget to remove it from the last part, and you should return all of this in a variable. |
```
Input: print_triangle(3, "*")
Output:
  *
 ***
*****

Input: print_triangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$
```

| Filename | Description/Task |
| --- | --- |
| <pre>[5-famous_cat.py](5-famous_cat.py)</pre><!--@schambig--> | In this challenge, you need to find the most famous kitty based on their number of followers. You will receive a list of dictionaries, each containing the following properties:<br> • `name`: the kitty's name.<br> • `followers`: a list of numbers, where each number represents the followers on a particular social network.<br> Your task is to return a list with the names of the cats that have only the highest number of followers. If there are two or more cats with the same maximum number of followers, you should include them in the resulting list, maintaining the order in which they appear in the input list. |
```
Input: find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])
Output: ["Luna"]

Input: find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])
Output: ["Milo", "Gizmo"]
```

| Filename | Description/Task |
| --- | --- |
| <pre>[6-get_average.py](6-get_average.py)</pre><!--@schambig--> | In this challenge, you will need to calculate the overall class average as well as the individual average for each student. For this purpose, you will be provided with a list of dictionaries, each of which represents a student and has the following properties:<br> • `name`: The student's name.<br> • `grades`: The grades for each subject of the student.<br> Based on this information, you should return a new dictionary that has the property `class_average` with the class average and a list of `students` with the students and their individual averages.<br> It's important to mention that the averages should be calculated accurately and rounded to two decimal places to ensure the tests pass without any issues. |
```
Input: get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])

Output: {
  "class_average": 88.17,
  "students": [
    {
      "name": "Pedro",
      "average": 88.75
    },
    {
      "name": "Jose",
      "average": 88.5
    },
    {
      "name": "Maria",
      "average": 87.25
    }
  ]
}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[7-packages_info.py](7-packages_info.py)</pre><!--@schambig--> | In this challenge, you are working for a cargo transport company that needs to keep a record of the packages being shipped on each trip. To achieve this, you will be provided with a list of tuples, each of which represents a package and includes the following properties:<br> • `id`, `weight`, `destination`<br> Based on this information, you need to create a function that calculates the total weight of the packages and the quantity of packages being sent to each destination. To do this, you should return a new dictionary with the following properties:<br> • `total_weight`: The total weight of the packages, rounded to two decimal places.<br> • `destinations`: A dictionary with destinations as keys and the quantity of packages as values.<br> It's important to note that the function should round the total weight to two decimal places, and each destination should appear only once in the dictionary. |
```
Input: get_packages_info([
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
])

Output: {
  "total_weight": 171.50,
  "destinations": {
    "Mexico": 3,
    "Colombia": 4,
    "Argentina": 3
  }
}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[8-count_letters.py](8-count_letters.py)</pre><!--@schambig--> | In this challenge, you will need to implement the logic for a function that counts the occurrences of each letter in a text string and stores it in a dictionary.<br>It's important to mention that the function should be case-sensitive, meaning uppercase and lowercase letters should be considered different. |
```
Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[9-largest_palindrome.py](9-largest_palindrome.py)</pre><!--@schambig--> | In this challenge, you need to create a function that finds the longest palindrome in a list of words.<br> You will receive a single parameter: a list of words.<br> • If there are no palindromes in the list, the function should return None.<br> • If there are multiple palindromes with the same maximum length, you should return the first palindrome found in the list.<br> • A palindrome is a word that can be read the same way forwards and backward. |
```
Input: find_largest_palindrome(["racecar", "level", "world", "hello"])
Output: "racecar"

Input: find_largest_palindrome(["Hibou", "Python", "xml", "owl"])
Output: None
```

| Filename | Description/Task |
| --- | --- |
| <pre>[10-set_intersection.py](10-set_intersection.py)</pre><!--@schambig--> | In this challenge, you must implement the logic for the `find_set_intersection` function, which finds the intersection of sets in a list of sets.<br> You will receive a single parameter: a list of sets.<br> The function should find the intersection of all the sets in the list and return the result as a new set.<br> If the list is empty or if there is no intersection between the sets, the function should return an empty set |
```
Input: find_set_intersection([
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
])
Output: {3, 4}

Input: find_set_intersection([
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
])
Output: set()
```

| Filename | Description/Task |
| --- | --- |
| <pre>[11-two_vowels.py](11-two_vowels.py)</pre><!--@schambig--> | In this challenge, you must create the logic for the `find_words_with_two_vowels` function, which finds words that contain exactly two vowels in a list of words.<br> The vowels can be either uppercase or lowercase.<br> You will receive a single parameter: a list of words.<br> The function should return a new list that contains all the words from the original list that meet the condition mentioned above.<br> If there are no words that meet this condition, you should return an empty list. |
```
Input: find_words_with_two_vowels([
  "hello",
  "Salo",
  "world",
  "Hibou"
])
Output: ['hello', 'Salo']

Input: (find_words_with_two_vowels([
    "text",
    "test",
    "python",
    "example"
])
Output: []
```

| Filename | Description/Task |
| --- | --- |
| <pre>[12-words_length.py](12-words_length.py)</pre><!--@schambig--> | In this challenge, you need to create a function called `count_words_by_length` that takes a list of words and returns a dictionary that maps the length of the words to the count of words having that length. |
```
Input: count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])
Output: {5: 1, 6: 2, 10: 1, 4: 2}

Input: count_words_by_length([
  "apple",
  "banana",
  "orange"
])
Output: {5: 1, 6: 2}
```
| Filename | Description/Task |
| --- | --- |
| <pre>[13-filter_message.py](13-filter_message.py)</pre><!--@schambig--> | In this challenge, you will implement a function that filters messages for a specific user.<br> The `filter_user_messages` function will receive two parameters<br> • `messages`: a list of messages.<br> • `user`: a username.<br> It should return a new list containing only the messages from the specified user.<br> The messages list contains dictionaries with information about each message, including the `sender` and the message `content`.<br> In case no messages from the user are found, the function should return an empty list `[]`. |
```
Input:
messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]
user = 'Alice'
print(filter_user_messages(messages, user))

Output:
[
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]
```

| Filename | Description/Task |
| --- | --- |
| <pre>[14-my_map.py](14-my_map.py)</pre><!--@schambig--> | In this challenge, you will need to implement a custom function that emulates the behavior of the map method using higher-order functions.<br> The function will take two parameters: a list and a function (func).<br> • The `list` will contain a set of elements (numbers, objects, strings, etc.)<br> • The function will be used to perform a specific action on each element of the list.<br> The goal is to return a new list with the results obtained from applying the function to each element, similar to how the map method would do it. |
```
Input: my_map([1, 2, 3, 4], lambda num: num * 2)
Output: [2, 4, 6, 8]

Input: my_map([
{"name": "colas", "age": 3},
{"name": "pequeña", "age": 4},
{"name": "blanca", "age": 3},
{"name": "manchas", "age": 2}],
lambda pet: pet["name"])
Output: ['colas', 'pequeña', 'blanca', 'manchas']
```

| Filename | Description/Task |
| --- | --- |
| <pre>[15-try_except.py](15-try_except.py)</pre><!--@schambig--> | In this challenge, you need to create a function called `calculate_average` that calculates the average of a list of numbers. However, the function should handle two special cases correctly:<br> • If the list is empty, the function should raise a ValueError exception with the message "The list is empty."<br> • If the list contains elements that are not numbers, the function should raise a TypeError exception with the message "The list contains non-numeric elements."<br> Your goal is to implement the `calculate_average` function in a way that properly handles these cases and returns the average of the numbers in the list. |
```
Input: calculate_average([1, 2, 3, 4, 5])
Output: 3.0

Input: calculate_average([10, 20, 30, 40, 50])
Output: 30.0

Input: calculate_average([])
Output: ValueError: The list is empty.

Input: calculate_average([1, 2, '3', 4, 5])
Output: TypeError: The list contains non-numeric elements.
```

| Filename | Description/Task |
| --- | --- |
| <pre>[16-handle_exception.py](16-handle_exception.py)</pre><!--@schambig--> | In this challenge, you need to create a function called `calculate_discounted_price` that calculates the discounted price of a product.<br> The function will receive two parameters: `price and discount`.<br> Your goal is to implement the necessary logic to calculate the price with the applied discount.<br> However, there are some conditions and exception handling that you should take into account:<br> • If the price or discount is a negative value, you should raise a `ValueError` exception with the message "Price and discount must be positive values."<br> • If the price or discount is not a number, you should raise a `TypeError` exception with the message "Price and discount must be numbers."<br> • In the case of any other unforeseen exception, you should catch it and raise a generic `Exception` with the message "An unexpected error has occurred." followed by the original exception message for more details.<br> Your function should return the price with the applied discount.<br> If the calculation is successful, you should return the result.<br> If any exception occurs, you should propagate it so that it can be handled in the appropriate context. |
```
Input: calculate_discounted_price(100, 0.2)
Output: 80.0

Input: calculate_discounted_price(-50, 0.2)
Output: ValueError: Price and discount must be positive values.
```

| Filename | Description/Task |
| --- | --- |
| <pre>[17-task_mngr_closures.py](17-task_mngr_closures.py)</pre><!--@schambig--> | In this challenge, you will implement the logic of a task planner in Python.<br> The goal is to build the closure function called `createTaskPlanner`, which will return a series of methods to manage tasks.<br> Below are the methods that need to be implemented:<br> • `addTask(task)`: receives a dictionary containing task information and adds it to the array of tasks. The dictionary must contain the following keys: `'id'`, `'name'`, `'priority'`, `'tags'`, and `'completed'`. The `'completed'` key will be automatically set to `False` when adding a task.<br> • `removeTask(value)`: receives the `'id'` or `'name'` of the task and removes it from the array of tasks.<br> • `getTasks()`: returns the array of tasks.<br> • `getPendingTasks()`: returns only the pending tasks.<br> • `getCompletedTasks()`: returns only the completed tasks.<br> • `markTaskAsCompleted(value)`: receives the `'id'` or `'name'` of the task and marks it as completed.<br> • `getSortedTasksByPriority()`: returns a copy of the tasks sorted by priority (3: not very urgent, 2: urgent, 1: very urgent), without modifying the original list of tasks.<br> • `filterTasksByTag(tag)`: filters tasks by a specific tag.<br> • `updateTask(taskId, updates)`: searches for the task corresponding to the specified `'id'` and updates its properties with those specified in the updates dictionary. |
```
Input: 
planner = createTaskPlanner()
planner['addTask']({
    'id': 1,
    'name': 'Buy milk',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Do the chores',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Do the chores')
print(planner['getCompletedTasks']())

Output:
[{
  'id': 2,
  'name': 'Do the chores',
  'completed': True,
  'priority': 3,
  'tags': ['personal']
}]

===============================================

Input:
planner = createTaskPlanner()
planner['addTask']({
    'id': 1,
    'name': 'Buy milk',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Do the chores',
    'priority': 3,
    'tags': ['personal']
})

print(planner['filterTasksByTag']('shopping'))

Output:
[{
    'id': 1,
    'name': 'Buy milk',
    'completed': False,
    'priority': 1,
    'tags': ['shopping', 'home']
}]
```

| Filename | Description/Task |
| --- | --- |
| <pre>[18-car_class.py](18-car_class.py)</pre><!--@schambig--> | In this challenge, you will need to create the logic for a car using classes.<br> You should implement the necessary logic in the `Car` class in such a way that it can serve as a basis for creating new cars that receive the following parameters:<br> • `brand`: Car brand<br> • `model`: Car model<br> • `year`: Car year<br> • `mileage`: Car mileage<br> • `state`: The default state of the car will be  `False`, indicating that the car is turned off.<br> Additionally, you should implement the following methods to make the vehicles created with the `Car` class functional:<br> • `turnOn()`: A method that will turn on the car.<br> • `turnOff()`: A method that will turn off the car.<br> • `drive(kilometers)`: With this method, we can increase the mileage according to the given kilometers, but only if the car is turned on. Otherwise, it should display the following error message: "The car is off."<br> Remember to handle errors as an Exception. |
```
Input:
toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOn();
toyota.drive(100);
toyota.mileage

Output: 100
===========================================
Input:
toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOff()
toyota.drive(100)

Output: Exception: The vehicle is off
```

| Filename | Description/Task |
| --- | --- |
| <pre>[19-shopping_cart.py](19-shopping_cart.py)</pre><!--@schambig--> | In this challenge, you must create a shopping cart system.<br> Also you need to create a file named [`product.py`](https://github.com/schambig/python_workout/blob/main/basic_challenges/product.py), which will be the base and abstract class.<br> You should create the child classes `Article` and `Service` that will extend from Product.<br> The `Article` class should implement the `addToCart()` method in a way that returns the string "Adding x units of article x to the cart," where `x` is the name and quantity of the product. On the other hand, the `Service` class should implement the `addToCart()` method in a way that returns the string "Adding service x to the cart," where `x` is the name of the service.<br> In addition, you should create the `Cart` class, which will be the shopping cart and will have the following methods:<br> • `addProduct(product)`: This method will add a product to the end of the shopping list and should call the `addToCart()` method of each product or service.<br> • `deleteProduct(product)`: This method will receive a product and remove it from the list of products.<br> • `calculateTotal()`: This method will calculate the total of the added products and return it.<br> • `getProducts()`: This method will return the array of products contained in the cart. |
```
Input:
book = Article("Libro", 100, 2);
course = Service("Curso", 120, 1);

cart = Cart();
cart.addProduct(book);
cart.addProduct(course);
cart.calculateTotal();

Output:
Adding 2 units of the article Book to the cart
Adding service Course to the cart
320
==================================================
Input:
book = Article("Libro", 100, 2);
course = Service("Curso", 120, 1);

cart = Cart();
cart.addProduct(book);
cart.addProduct(course);
cart.deleteProduct(book);
cart.calculateTotal();

Output:
Adding 2 units of the article Book to the cart
Adding service Course to the cart
120
```

| Filename | Description/Task |
| --- | --- |
| <pre>[20-usr_encapsulation.py](20-usr_encapsulation.py)</pre><!--@schambig--> | In this challenge, you must implement the logic for the `User` class that represents a user in a social network and use encapsulation to protect their private data.<br> The class should have the following private variables:<br> • `name`<br> • `age`<br> • `friends` (a list of dictionaries representing Users)<br> • `messages ` (a list of strings)<br> Additionally, you should provide the following public methods:<br> • `addFriend(friend)`: adds a user to the current user's list of friends.<br> • `sendMessage(message, friend)`: adds a message to the current user's message list and to the specified friend.<br> • `showMessages()`: returns the list of messages for the current user.<br> You should also have defined `getters` and `setters` to access private data such as `name` and `age`, which can be modified using their respective setter methods. |
```
Input:
usr1 = User("Mike", 28)
usr2 = User("Louis", 45)
usr1.addFriend(usr2)
usr1.sendMessage("Whatup fool", usr2)

usr1.showMessages()

Output:
["Whatup fool"]
=============================================
Input:
usr3 = User("Mike", 28)
usr3.name = "Michael"
print(usr3.name)

Output:
Michael
```

| Filename | Description/Task |
| --- | --- |
| <pre>[21-animal_inheritance.py](21-animal_inheritance.py)</pre><!--@schambig--> | In this challenge, you need to create a class hierarchy using inheritance.<br> The base class will be `Animal` with properties:<br> • `name`, `age`, and `specie`<br> • As well as a method `getInfo` that returns an object with the animal's information.<br> Next, you should create a class `Mammal` that inherits from `Animal` and has an additional property `hasFur`.<br> It should also have a method `getInfo` that overrides the parent's method and includes information about `hasFur`.<br> Finally, create a class `Dog` that inherits from `Mammal` and has an additional property `breed`. Its `getInfo` method should override the parent's method and include information about `breed`.<br> Additionally, it should have a `bark` method that returns the string `"woof!"`. The properties `specie` and `hasFur` should be included as `"dog"` and `True`, respectively, in the implementation, so it should not be necessary to pass these values when creating an instance. |
```
Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:
{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}
============================================
Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:
{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}
============================================
Input:
dog = Dog("colitas", 4, "chusquita");
dog.bark()

Output:
"woof!"
```

| Filename | Description/Task |
| --- | --- |
| <pre>[22-payment_polimorphism.py](22-payment_polimorphism.py)</pre><!--@schambig--> | In this challenge, you will have to implement a payment system using polymorphism.<br> You should create a base class called `Pay` that contains a single method called `make_pay`.<br> This method will receive the payment amount and return an object with two properties:<br> • `realized: True`<br> • `quantity: $amountToPay`<br><br> Additionally, you will need to create the classes `PayPal`, `Card`, and `Cash`, where each one should inherit from the `Pay` class.<br><br> The `PayPal` class should receive an `email` in the constructor, and the `make_pay` method should add the properties:<br> • `platform: 'PayPal'`<br> • `email: $ReceivedEmail`<br><br> The `Card` class will receive a 16-digit card number.<br> When accessing the `make_pay` method, it will validate if the card has this length.<br> If the card does not have 16 digits, an `Exception` should be raised.<br> Otherwise, the method from `Pay` will have an additional property called `last_card_numbers`, where the last 4 digits of the card will be returned.<br><br> The `Cash` class will simply return the same as the base class.<br><br> Finally, you must implement the logic of the  `process_pay` function, which will receive a payment method and the amount. It will return the object by calling the `make_pay` method of each received entity.<br><br> Note that each class should have its own file.<br> • [pay.py](https://github.com/schambig/python_workout/blob/main/basic_challenges/pay.py)<br> • [paypal.py](https://github.com/schambig/python_workout/blob/main/basic_challenges/paypal.py)<br> • [card.py](https://github.com/schambig/python_workout/blob/main/basic_challenges/card.py)<br> • [cash.py](https://github.com/schambig/python_workout/blob/main/basic_challenges/cash.py) |
```
Input:
card = Card("4913478952471122")
process_pay(card, 100)

Output:
{
  realized: True,
  quantity: 100,
  last_card_numbers: "1122",
}
================================
Input:
paypal = PayPal("test@mail.com")
process_pay(paypal, 240)

Output:
{
  realized: True,
  quantity: 240,
  platform: "PayPal",
  email: "test@mail.com",
}
================================
Input:
cash = Cash()
process_pay(cash, 400)

Output:
{
  realized: True,
  quantity: 400,
}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[23-my_dictionary.py](23-my_dictionary.py)</pre><!--@schambig--> | In this callenge your goal is to create a class called `MyDict` that simulates the behavior of a native Python dictionary, without using the existing methods. You will implement the logic for the following methods:<br> • `map(func)`: Iterates over each element of our data structure, applying the function `func` to each one, and returns a new list (which will be an instance of `MyDict`).<br> • `filter(func)`: Iterates over each element of our data structure, filtering them according to the conditions specified by the function `func`, and returns a list with the filtered elements (also an instance of `MyDict`).<br> • `join(character)`: Concatenates all elements of our data structure into a string, separating them by the specified `character`. If no character is provided, the default separator will be a comma `,`.<br> • `append(item)`: Adds an element (`item`) to the end of the list and increases the `length`.<br> • `pop()`: Removes the last element from the list and returns it, also decreasing the `length`.<br> • `shift()`: Removes the first element from the list and returns it, decreasing the `length`.<br> • `unshift(item)`: Adds an element (`item`) to the beginning of the list and increases the `length`.<br> Additionally, you need to store the elements within the property named `data` and the number of elements within the property named `length` so that they can be accessed during testing. |
```
Input:
myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

print(myList.data)

Output:
{0: 'a', 1: 'b', 2: 'c'}
========================
Input:
myList = MyList()
myList.append('Hola')
myList.unshift('k ase')

print(myArray.data)

Output:
{0: 'Hola', 1: 'k ase'}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[24-contacts_hash_table.py](24-contacts_hash_table.py)</pre><!--@schambig--> | In this challenge, you must build a contact list using a hash table.<br> Your goal is to implement the logic for the `ContactList` class to add contacts and perform the corresponding operations.<br> The hash table (`ContactList`) should have the following methods:<br> • `hash(key)`: This method will take a `key` (in this case the `name` of the contact) and compute its hash value using the built-in `hash` function.br> • `insert(name, phone)`: This method will receive the name and phone number of a contact and add the contact to the hash table.<br> • `get(name)`: This method will receive the name of a contact and return its phone number. If the contact does not exist, it will return `None`.<br> • `retrieve_all()`: This method will return a list with all the buckets used in the hash table.<br> • `delete(name)`: This method will receive the name of a contact and remove that contact from the hash table. If the name is not found, it should return `None`. |
```
Input:
contactList = ContactList(5)
contactList.insert("Mrs Pequeña", "666-555-444")

contactList.retrieveAll()

Output:
[['Mrs Pequeña', '666-555-444']]
================================================
Input:
contactList = ContactList(5)
contactList.insert("Mrs Pequeña", "666-555-444")

contactList.get("Mrs Pequeña")

Output:
666-555-444"
================================================
Input:
contactList = ContactList(5)
contactList.insert("Mrs Pequeña", "666-555-444")
contactList.delete("Mrs Pequeña")

contactList.get("Mrs Pequeña")

Output:
None
```

| Filename | Description/Task |
| --- | --- |
| <pre>[25-task_mngr_maps.py](25-task_mngr_maps.py)</pre><!--@schambig--> | In this challenge, you need to create a task organizer using Maps and Sets in Python. Instead of using closures, we will implement a class-based solution that contains two methods:<br> • The `add_task` method will handle adding tasks to the Map. It is important to convert all letters in the task to lowercase using `lower()` to check if the task already exists. If it exists, the new tags will be added to the corresponding Set. If the task does not exist, a new entry in the Map will be created with a Set of tags initialized with the provided tags.<br> • The `print_tasks` method will return all created tasks with their tags. |
```
Input:
my_task_manager = TaskManager()

my_task_manager.add_task('Buy Milk', ['shopping', 'urgent'])
my_task_manager.add_task('Walk the Dog', ['pets'])
my_task_manager.add_task('Workout', ['health'])

my_task_manager.print_tasks()

Output:
{
  'buy milk': {'shopping', 'urgent'},
  'walk the dog': {'pets'},
  'workout': {'health'}
}
============================================================
Input:
my_task_manager = TaskManager()

my_task_manager.add_task('Buy Milk', ['shopping', 'urgent'])
my_task_manager.add_task('Walk the Dog', ['pets'])
my_task_manager.add_task('Buy Milk', ['dairy'])
my_task_manager.add_task('Workout', ['health'])

my_task_manager.print_tasks()

Output:
{
  'buy milk': {'dairy', 'shopping', 'urgent'},
  'walk the dog': {'pets'},
  'workout': {'health'}
}
```

| Filename | Description/Task |
| --- | --- |
| <pre>[26-single_linked_list.py](26-single_linked_list.py)</pre><!--@schambig--> | In this challenge, we will implement a simple linked list to store information about patients in a hospital. Each node in the list will represent a patient and will have the following fields:<br> • Patient's name (string)<br> • Patient's age (number)<br> • Bed number assigned to the patient (number)<br><br> The linked list should have the following methods:<br> • `add_patient(name, age)`: Adds a new patient to the list, assigning them the next available bed. If there are no available beds, it should raise an error with the message "No beds available".<br> • `remove_patient(name)`: Removes the patient with the specified name from the list and frees up their bed. If the patient is not found in the list, it should raise an error with the message "Patient not found".<br> • `get_patient(name)`: Returns the information of the patient with the specified name in the following format `{name, age, bedNumber}`. If the patient is not found in the list, it should raise an error with the message "Patient not found".<br> • `getPatientList()`: Returns a list with the information of all patients in the list, where each patient has the following format `{name, age, bedNumber}`.<br> • `get_available_beds(): Returns a number indicating the total number of available beds.<br> Remember to use the syntax raise Exception("message") to raise errors. |
```
Input:
lista = PatientList(3)
lista.add_patient("Patient 1", 20)
lista.add_patient("Patient 2", 30)

list.get_patient_list()

Output:
[
  { 'name': 'Patiente 1', 'age': 20, 'bed_number': 1 },
  { 'name': 'Patiente 2', 'age': 30, 'bed_number': 2 },
]

list.get_patient("Patiente 1")

Output:
{ 'name': 'Patiente 1', 'age': 20, 'bed_number': 1 }

list.remove_patient("Patiente 1")

list.get_patient_list()

Output:
[
  { 'name': 'Patiente 2', 'age': 30, 'bed_number': 2 },
]
```

| Filename | Description/Task |
| --- | --- |
| <pre>[27-playlist_stack.py](27-playlist_stack.py)</pre><!--@schambig--> | In this challenge, you are requested to implement a playlist using a stack in Python.<br> You should create the `Playlist` class with the following properties:<br> • `top`, `bottom`, and `length`, to represent the top, bottom, and length of the stack, respectively.<br> The `Playlist` class should have the following methods:<br> • `add_song(song)` : This method allows adding a song to the stack. The song is added to the top of the stack.<br> • `play_song()`: This method allows playing the song at the top of the stack and then removing it. If the stack is empty, an error should be raised with the message "There is no song in the playlist."<br> • `getPlaylist()`: This method transforms the stack into a list (array) containing all the songs in the order of playback, from the most recently added to the first. |
```
Input:
playlist = Playlist()

playlist.addSong("Sprinter")
playlist.addSong("Yellow Ferrari")
playlist.addSong("Phospholipid")

Output:
print(playlist.playSong())  # Phospholipid
print(playlist.playSong())  # Yellow Ferrari
print(playlist.playSong())  # Sprinter
print(playlist.playSong())  # Exception: There is no song in the playlist.
==========================================================================
Input:

playlist = Playlist()

playlist.addSong("Sprinter")
playlist.addSong("Yellow Ferrari")
playlist.addSong("Phospholipid")

print(playlist.getPlaylist()) 
Output: ["Phospholipid", "Yellow Ferrari", "Sprinter"]
```

| Filename | Description/Task |
| --- | --- |
| <pre>[]()</pre><!--@schambig--> |  |
```
```

<!-- <pre><br><br></pre> • <br>•-->


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
