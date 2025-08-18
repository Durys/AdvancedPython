from linked_list import LinkedList
from node import Node


class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.set_next(Node(value, prev=self.tail))
            self.tail = self.tail.next
        return self.tail

    def __str__(self):
        listed = [str(x) for x in self]
        return " <-> ".join(listed)


if __name__ == "__main__":
    dl = DoublyLinkedList([2, 3, 4, 5])
    print(dl)
    for d in dl:
        if d.prev is None:
            print("This is the head node - it has no previous values")
        else:
            print(d.prev)
