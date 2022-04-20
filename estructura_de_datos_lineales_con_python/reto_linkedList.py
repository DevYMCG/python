from array_clase import Array
from linked_list import SinglyLinkedList

class SinglyLinkedListArray:

    def __init__(self, rows, fill_value=None):
        self.data = Array(rows)

        for i in range(rows):
            self.data.__setitem__(i, '*')
        
        self.list = SinglyLinkedList()

        for i in range(rows):
            self.list.append(self.data.items[i])
        
        for number in self.list.iter():
            print(number)


if __name__ == "__main__":

    array = SinglyLinkedListArray(5)

