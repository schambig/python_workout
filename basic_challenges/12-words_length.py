#!/usr/bin/python3

# One liner
def count_words_by_length(words):
  return {len(w): sum(1 for i in words if len(i) == len(w)) for w in words}

# Short version using list and dictionary comprehensions.
def count_words_by_length(words):
  keys = [len(w) for w in words]
  return {k: keys.count(k) for k in keys}

# Large version using loop and conditional.
def count_words_by_length(words):
  dic = {}
  for w in words:
    key = len(w)
    if key not in dic:
      dic[key] = 1
    else:
      dic[key] += 1
  return dic


print(count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
]))

print(count_words_by_length([
  "apple",
  "banana",
  "orange"
]))
