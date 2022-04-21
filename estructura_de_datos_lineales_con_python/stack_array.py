from array_clase import Array

class Stack:
    def __init__(self, capacity, fill_value=None):
        self.top = None
        self.size = 0
        self.capacity = capacity

        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        
    
    def push(self, index, data):
        self.items[index] = data
        self.top = data
        self.size += 1
    
    def __len__(self):
        """Returns capacity of the array."""
        return len(self.items)
    
    def pop(self):
        if self.pop:
            for i in range(self.capacity-1, -1, -1):
                if self.items[i] != None:
                    self.items[i] = None
                    self.size -= 1
                if i > 0:
                    self.top = self.items[i-1]
                else:
                    self.top = None
                break
        else:
            return "The stack is empty"
    
    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)

    def peek(self):
        if self.top:
            return self.top
        else:
            return "The stack is empty"
    
    def clear(self):
        while self.top:
            self.pop()


if __name__ == "__main__": 
    menu = Stack(5)
    print(menu.__str__())
    menu.push(1,'egg')
    print(menu.__str__())
    # print(menu.__len__())
    print(menu.pop())
    print(menu.__str__())

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