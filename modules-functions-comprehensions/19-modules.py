import sys
print('path:', sys.path)
# path: ['/home/salomon/githubRepos/python_workout/modules-functions-comprehensions', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload',
#        '/home/salomon/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

import re
text = 'Mi numero de telefono es 999 555 444, el codigo del pais es 51, mi numero de la suerte 7'
result = re.findall('[0-9]+', text)
print(result) # ['999', '555', '444', '51', '7']

import time
timestamp = time.time()
print(timestamp) # 1687630867.5273066

local = time.localtime()
print(local)
#time.struct_time(tm_year=2023, tm_mon=6, tm_mday=24, tm_hour=13, tm_min=21, tm_sec=7, tm_wday=5, tm_yday=175, tm_isdst=0)
result = time.asctime(local)
print(result) # Sat Jun 24 13:21:07 2023

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter) # Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})