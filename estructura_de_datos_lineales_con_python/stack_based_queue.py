class Queue:
    def __init__(self):
        self.inboud_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inboud_stack.append(data)
    
    def dequeue(self):
        if not self.outbound_stack: 
            while self.inboud_stack:
                self.outbound_stack.append(self.inboud_stack.pop())
        
        return self.outbound_stack.pop()

"""
>>> from stack_based_queue import Queue
>>> numbers = Queue()
>>> numbers.enqueue(5)
>>> numbers.enqueue(6)
>>> numbers.enqueue(7)
>>> print(numbers.inboud_stack)
[5, 6, 7]
>>> numbers.dequeue()
5
# esta vacio por que con el ciclo while hicimos pop a cada elemento
>>> print(numbers.inboud_stack)
[]
# pasaron de un stack al otro
>>> print(numbers.outbound_stack)
[7, 6]
>>> numbers.dequeue()
6
>>> print(numbers.outbound_stack)
[7]
>>> numbers.dequeue()           
7                               
>>> print(numbers.inboud_stack) 
[]                              
>>>                             
"""