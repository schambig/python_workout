'''
Logical Operators (to compare Boolean types), we get a Boolean value as result
and, or, not
'''

# With 'and' all must be True in order to get True
# It will return False if there is at least one False
final_result = True and True and 10 > 20
print(final_result)

# Using 'or' we'll get True if there is at least one True value
final_result = False or False or 10 < 20
print(final_result)

# Conbining Logical Operators using parenthesis
final_result = True and (False or 5 > 10)
print(final_result)

# Using 'not' to change a boolean value to its counterpart
final_result = not False
print(final_result)
