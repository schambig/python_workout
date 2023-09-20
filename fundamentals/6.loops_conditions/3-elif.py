'''
`elif` is a shortened form of "else if."
It is a keyword used in conjunction with the `if` statement to check multiple
conditions in a sequence.
The elif statement allows you to test additional conditions after the initial `if` condition,
and it is only evaluated if the preceding if or elif conditions are not met.

if condition1:
    # Code block to execute if condition1 is True
elif condition2:
    # Code block to execute if condition2 is True
elif condition3:
    # Code block to execute if condition3 is True
# ...
else:
    # Code block to execute if none of the above conditions are True
'''

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
