from node import Node
from linked_list import LinkedList


## THIS SOLUTION IS IMPERFECT - THE TAIL OF THE LIST WILL HAVE NONE AS ITS NEXT NODE BEFORE RUNNING COMPLETE_LOOP...


class CircularLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.set_next(Node(value, prev=self.tail))
            self.tail = self.tail.next
            self.head.set_prev(self.tail)
        return self.tail

    def __str__(self):
        listed = []
        br = None
        for it in self:
            if br is None:
                listed.append(str(it.value))
            else:
                break
        return " <-> ".join(listed)


if __name__ == "__main__":
    cl = CircularLinkedList([2])
    cl.add(4)
    cl.add(3)
    cl.add(-5)
    print(cl)
    for c in cl:
        print("prev: ", c.prev, " next: ", c.next)
