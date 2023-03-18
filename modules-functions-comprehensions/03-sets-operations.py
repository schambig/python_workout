set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b) # Using method
print(set_c) # {'mex', 'bol', 'pe', 'col'}
print(set_a | set_b) # Using operator | : {'mex', 'bol', 'pe', 'col'}

set_c = set_a.intersection(set_b) # Using method
print(set_c) # {'bol'}
print(set_a & set_b)# Using operator & : # {'bol'}

set_c = set_a.difference(set_b) # Using method
print(set_c) # {'mex', 'col'}
print(set_a - set_b) # Using operator - : {'mex', 'col'}

set_c = set_a.symmetric_difference(set_b) # Using method
print(set_c) # {'col', 'pe', 'mex'}
print(set_a ^ set_b) # Using operator ^ : {'col', 'pe', 'mex'}

# More about operations on sets:
# https://realpython.com/python-sets/#operating-on-a-set:~:text=in%20x%0AFalse-,Operating%20on%20a%20Set,-Many%20of%20the