class TwoWayNode(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data

"""
λ py
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from node_based_queue import Queue
>>> food = Queue()
>>> food.enqueue('eggs')
>>> food.enqueue('ham')
>>> food.enqueue('spam')
>>> food.head
<node_based_queue.TwoWayNode object at 0x00000137E26E2AD0>
>>> food.head.data
'eggs'
>>> food.head.next.data    
'ham'                      
>>> food.tail.data         
'spam'                     
>>> food.tail.previous.data
'ham'                      
>>>  
>>> food.count
3
>>> food.dequeue()
'eggs'
>>>                      
"""
