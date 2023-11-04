#!/usr/bin/python3

# If the .count() method is used,
# a count will be made on the string for each character traversed in the string's for loop,
# resulting in an algorithm with a complexity of O(n²).
def count_letters(phrase):
    return {char: phrase.count(char) for char in phrase}

# # If we use the dictionary.get() method,
# # the value of each character will be summed in a single total iteration of the string,
# # resulting in a complexity of O(n).
# def count_letters(phrase):
#   dic = {}
#   for i in phrase:
#     dic[i] = dic.get(i, 0) + 1
#   return dic

# Performance is better with the second function.
# While in this very simple example there is no noticeable difference,
# it will be useful to keep in mind when iterating and creating much larger and more complex elements.

# print(count_letters("Hola mundo"))
# print(count_letters("Hello world"))
