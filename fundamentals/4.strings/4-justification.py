'''
We can justify string in Python using:
ljust() to left justify
rjust() to right justify
center() to center
Note that these methods don't modify the original string (strings are inmmutable)
so a new one is created
'''

message = 'Hello World!'

message1 = message.ljust(20) # 20 spaces to the left
print(message1, '.')

message2 = message.rjust(20) # 20 spaces to the right
print(message2)

message3 = message.center(20) # 10 to the left and 20 to the right
print(message3)
