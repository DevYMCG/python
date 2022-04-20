from locale import currency
from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next
            
            current.next = node

        self.size +=1
    
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            
            previous = current
            current = current.next
    
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


"""
λ py
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from linked_list import SinglyLinkedList
>>> words = SinglyLinkedList()
>>> words.append('egg')
>>> words.append('ham')
>>> words.append('spam')
>>> current = words.tail
>>> while current:
...     print(current.data)
...     current = current.next
...
egg
ham
spam
>>> for word in words.iter():
...     print(word)
...
egg
ham
spam
>>> words.search('spam')
Data spam found!
>>> words.search('juice')
>>> words.clear()
>>> while current:
...     print(current.data)
...
"""
