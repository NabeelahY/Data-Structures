import sys
sys.path.insert(1, '../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = self.storage.__len__()

    def pop(self):
        self.size = self.storage.__len__()
        if self.storage.head is None:
            return
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.storage.__len__()
