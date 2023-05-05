numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers) # [2, 4]
print(numbers) # [1, 2, 3, 4, 5] filter doesn't change the original list


# More info about filter function:
# https://www.w3schools.com/python/ref_func_filter.asp