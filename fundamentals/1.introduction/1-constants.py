'''
A constant can not change (definition)
Constants do not exist in Python
The Python convention is to use UPPERCASE letters
It tends to be used just for read purposes
'''

COURSE_TITLE = 'Fundamental Python Practice'

print(COURSE_TITLE)

'''
List of Python Keywords:
Keywords are the reserved words in Python. We cannot use a keyword as a variable name,
function name or any other identifier.

False     await       else        import      pass
None      break       except      in          raise
True      class       finally     is          return
and       continue    for         lambda      try
as        def         from        nonlocal    while
assert    del         global      not         with
async     elif        if          or          yield
'''

'''
The above keywords may get altered in different versions of Python.
Some extra might get added or some might be removed.
You can always get the list of keywords in your current version by typing the following in the prompt.
'''

import keyword
print(keyword.kwlist)
