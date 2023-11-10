#!/usr/bin/python3
import re


# Using loops and conditionals
def find_words_with_two_vowels(words):
    vow = 'AEIOUaeiou'
    res = []
    for word in words:
        count = 0
        for c in word:
            if c in vow:
                count += 1
        if count == 2:
            res.append(word)
    return res

# Using two comprehensions
def find_words_with_two_vowels2(words):
    return [w for w in words if sum(c in 'AEIOUaeiou' for c in w) == 2]

# A variation of the above method, here we use 1 in the sum() function as a way to count occurrences of vowels in each word.
def find_words_with_two_vowels3(words):
    return [w for w in words if sum(1 for c in w if c in 'AEIOUaeiou') == 2]

# Using regular expressions (regex) library
# The use of a raw string (with r) is generally recommended when working with regular expressions
# because it helps avoid issues related to backslashes that might need to be escaped. (in this case it's no crucial but recommended) 
def find_words_with_two_vowels4(words):
    return [w for w in words if len(re.findall(r"[AEIOUaeiou]", w)) == 2]


print(find_words_with_two_vowels([
  "hello",
  "Salo",
  "world",
  "Hibou"
]))

print(find_words_with_two_vowels([
    "text",
    "test",
    "python",
    "example"
]))
