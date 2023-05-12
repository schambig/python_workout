# import functools
from functools import reduce 

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

# result = functools.reduce(accum, numbers)
result = reduce(accum, numbers)
# result = accum(accum(accum(accum(0, 1), 2), 3), 4) # this is what happens
# Look at this pic to better understand:
# https://drive.google.com/file/d/1A3LatTN-BrCrgmn-uATTthBG3iD_vG-G/view?usp=sharing 
print(result)
# counter =>  1
# item =>  2
# counter =>  3
# item =>  3
# counter =>  6
# item =>  4
# 10

# Now let's create a lambda function instead of 'def accum()'
res = reduce(lambda count, item: count + item, numbers)
print(res) # 10