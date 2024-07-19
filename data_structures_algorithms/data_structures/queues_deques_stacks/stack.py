# FOLLOWS LIFO

"""A stack can be implemented using deque - because it follows LIFO, only append and pop can be used."""


class Stack:
    def __init__(self, values):
        # Does it even have a head and tail naming?
        self.head = None
        self.tail = None

    def push(self):
        # Same as add
        pass

    def pop(self):
        pass

    def peek(self):
        return self.head