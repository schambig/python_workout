"""
Code used to create 'Node' class.

All the code but the 'Node' class is written in the shell
for demonstrative purposes.

The node methods should be incorporated into the Node class.
"""

class Node():
    """Represents a single linked node."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# # Creating 3 differents nodes 
# node1 = None
# node2 = Node("A", None)
# node3 = Node("B", node2)

# # This causes an Atribute Error
# # node1.next = node3

# node1 = Node("C", node3)

# # Now we can check, node, node data and next
# node2
# node2.data
# node2.next
# node3.next
# node3.next.data


# Create a series of nodes using a for loop
# for count in range(1, 6):
#     head = Node(count, head)

# this will throw an error:
#   Traceback (most recent call last):
#     File "<stdin>", line 2, in <module>
#   NameError: name 'head' is not defined
# meaning we need to create head = None, just for this to work
# so: head = None
# now we can use our for loop and print our node values with:
#     while head != None:
#         print(head.data)
#         head = head.next
