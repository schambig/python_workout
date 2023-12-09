#!/usr/bin/python3

# short version
# If the count() method is used,
# a count will be made on the string for each character traversed in the string's for loop,
# resulting in an algorithm with a complexity of O(n²).
def count_letters(phrase):
    return {char: phrase.count(char) for char in phrase}

# long version
# # If we use the get() method,
# # the value of each character will be summed in a single total iteration of the string,
# # resulting in a complexity of O(n).
def count_letters(phrase):
  dic = {}
  for i in phrase:
    dic[i] = dic.get(i, 0) + 1
  return dic

'''
line 17 translates to:

    # Assume i = 'r'
    if 'r' in dic:
        dic['r'] = dic['r'] + 1  # Increment the count for 'r'
    else:
        dic['r'] = 0 + 1         # Initialize the count for 'r' to 0 and then increment it

Now, let's consider this process for the letter 'r' in the context of a loop.
If the letter 'r' is encountered multiple times in the loop,
the count will be incremented each time:
    1.First encounter (assuming dic is initially empty):
        - 'r' is not in dic, so it initializes the count to 0 and increments it by 1.
        - Result: dic['r'] = 1
    2.Second encounter (assuming dic is now {'r': 1}):
        - 'r' is in dic, so it increments the count by 1.
        - Result: dic['r'] = 2
    3.Third encounter (assuming dic is now {'r': 2}):
        - 'r' is in dic, so it increments the count by 1.
        - Result: dic['r'] = 3
''' 

'''
Performance is better with the second function.
While in this very simple example there is no noticeable difference,
it will be useful to keep in mind when iterating and creating much larger and more complex
elements.
'''


print(count_letters("Hola mundo"))
print(count_letters("Hello world"))
