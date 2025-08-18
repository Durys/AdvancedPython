class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def __str__(self):
        return str(self.value)

