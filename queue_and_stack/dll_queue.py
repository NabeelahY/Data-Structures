import sys
sys.path.insert(1, '../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.__len__()

    def dequeue(self):
        self.size = self.storage.__len__()
        if self.storage.head is None:
            return
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.storage.__len__()
