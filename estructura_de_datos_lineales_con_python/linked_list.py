"""
Code used for the class 'Nodos y singly linked list'.

All the code but the 'Node' class is written in the shell
for demonstrative purposes.

The node methods should be incorporated into the Node class.
"""
from node import Node

class SinglyLinkedList:

    def __init__(self):
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """ añadir nodos """
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                """ si el retorno de su valor no es falso"""
                current = current.next
            
            current.next = node

        self.size +=1
    
    def size(self):
        """ retorna el tamaño de los nodos"""
        return str(self.size)
    
    def iter(self):
        """ metodo iterador """
        current = self.tail

        while current:
            val = current.data
            current = current.next
            """ Generador de valores los almacena sobre la marcha"""
            yield val
    
    def delete(self, data):
        """Eliminar nodos"""
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                """ Si es igual al dato que pasamos como argumento"""
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            
            previous = current
            current = current.next
    
    def search(self, data):
        """ Busqueda de nodo con el valor"""
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")
    
    def clear(self):
        """ limpiar nuestra lista"""
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
