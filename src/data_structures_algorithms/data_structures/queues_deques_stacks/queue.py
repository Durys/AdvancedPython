# FOLLOWS FIFO

"""A stack can be implemented using deque - because it follows FIFO, only append and popLeft can be used."""


# TODO: FIX A BIT BASING ON STACK

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self, values):
        self.bottom = None
        self.top = None

        for v in values:
            self.enqueue(v)

    def __str__(self):
        res = [str(x.value) for x in self]
        return " -> ".join(res)

    def __iter__(self):
        current = self.bottom
        while current:
            yield current
            current = current.next

    def __len__(self):
        res = 0
        current = self.bottom
        while current:
            res += 1
            current = current.next
        return res

    def enqueue(self, value):
        if self.bottom is None:
            self.bottom = self.top = Node(value)
        else:
            self.top.next = Node(value)
            self.top = self.top.next
        return self.top

    def dequeue(self):
        if not self.is_empty():
            self.bottom = self.bottom.next

    def peek(self):
        if not self.is_empty():
            return self.bottom

    def is_empty(self):
        if len(self) != 0:
            return False
        return True


if __name__ == "__main__":
    s = Queue(["2", "3", "4"])
    print(s)
    s.enqueue("5")
    print(s)
    s.dequeue()
    print(s)
