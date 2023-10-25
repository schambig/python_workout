#!/usr/bin/python3

# short version (In python ternary operator use if and else and not ? and :)
def is_leap_year(year):
    if year > 0:
        return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False
    return False


# # large version
# def is_leap_year(year):
#     if year > 0:
#         if (year % 100 != 0 or year % 400 == 0) and year % 4 == 0:
#             return True
#         else:
#             return False
#     else:
#         return False

# print(is_leap_year(2000))
# print(is_leap_year(-2024))
# print(is_leap_year(1984.5))
