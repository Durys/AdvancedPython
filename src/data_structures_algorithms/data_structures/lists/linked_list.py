from node import Node


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            for v in values:
                self.add(v)

    def __iter__(self):
        current_head = self.head
        while current_head:
            yield current_head
            current_head = current_head.next

    def __str__(self):
        listed = [str(x) for x in self]
        return " -> ".join(listed)

    def __len__(self):
        l = 0
        start = self.head
        while start:
            l += 1
            start = start.next
        return l

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.set_next(Node(value))
            self.tail = self.tail.next
        return self.tail

    def return_values(self):
        return [x.value for x in self]


if __name__ == "__main__":
    l = LinkedList([2, 3, 4, 5, 3])
    print(l)
    l.add(4)
    l.add(-2)
    print(l.return_values())
