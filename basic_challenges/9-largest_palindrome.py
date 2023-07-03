#!/usr/bin/python3

# Longest version
def find_largest_palindrome(words):
  pals = [w for w in words if w == w[::-1]]
  pal = ""
  for p in pals:
    if len(p) > len(pal):
      pal = p
  return pal if pal else None

# # Using a conditional and max()
# def find_largest_palindrome(words):
#   pals = [w for w in words if w == w[::-1]]
#   if pals:
#     pal = max(pals, key=len)
#     return pal if pal else None

# # Shortest version, using max() in a better way  
# def find_largest_palindrome(words):
#   pals = [p for p in words if p == p[::-1]]
#   return max(pals, key=len, default=None)
  
# print(find_largest_palindrome(["racecar", "level", "world", "hello"]))
# print(find_largest_palindrome(["Hibou", "Python", "xml", "owl"]))
