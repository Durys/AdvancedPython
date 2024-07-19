# FOLLOWS FIFO

"""A stack can be implemented using deque - because it follows FIFO, only append and popLeft can be used."""


class Queue:
    def __init__(self, values):
        # Does it even have a head and tail naming?
        self.head = None
        self.tail = None

    def enqueue(self):
        # Same as add
        pass

    def dequeue(self):
        # Delete the head, replace the head with head.next
        pass

    def peek(self):
        return self.head
