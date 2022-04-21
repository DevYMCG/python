from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size +=1
    
    def pop(self):
        if self.pop:
            data = self.top.data
            self.size -=1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            
            return data
        
        else:
            return "The stack is empty"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
    
    def clear(self):
        while self.top:
            self.pop()


"""
λ py
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from stack import Stack
>>> food = Stack()
>>> food.push('egg')
>>> food.push('ham')
>>> food.push('spam')
>>> food.pop()
'spam'
>>> food.peek()
'ham'
>>> food.clear()
>>> food.peek()
'The stack is empty'
>>>
"""