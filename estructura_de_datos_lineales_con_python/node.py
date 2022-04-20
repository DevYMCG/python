class Node():

    """ En una serie de nodos el ultimo nodo nos va a llevar a None """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

"""
>>> from node import Node
>>> node1 = None
>>> node2 = Node("A", None)
>>> node3 = Node("B", node2)
>>> node2
<node.Node object at 0x00000216BCE62530>
>>> node2.data
'A'
>>> node2.next
>>> node3.next
<node.Node object at 0x00000216BCE62530>
>>> node3.next.data
'A'
>>> node1
>>> node1.next
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'next'
>>> node1 = Node("C", node3)
>>> node1.next.data
'B'
>>> node1.data
'C'
>>> head = None
>>> for count in range(1,5):
...     head = Node(count, head)
...
>>> while head != None:
...     print(head.data)
...     head = head.next
...
4
3
2
1
"""

         
         