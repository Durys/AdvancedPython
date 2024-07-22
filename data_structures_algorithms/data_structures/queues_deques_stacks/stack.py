# FOLLOWS LIFO

"""A stack can be implemented using deque - because it follows LIFO, only append and pop can be used."""


class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class Stack:
    def __init__(self, values):
        self.top = None
        self._len = 0

        for v in values:
            self.push(v)

    def __str__(self):
        res = [str(x.value) for x in self]
        return " <- ".join(res)

    def __iter__(self):
        current = self.top
        while current:
            yield current
            current = current.prev

    def __len__(self):
        return self._len

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self._len += 1
        else:
            self.top = Node(value, self.top)
            self._len += 1

    def pop(self):
        if not self.is_empty():
            value = self.top.value
            self.top = self.top.prev
            self._len -= 1
        return value

    def peek(self):
        if not self.is_empty():
            return self.top

    def is_empty(self):
        if self._len != 0:
            return False
        return True


if __name__ == "__main__":
    s = Stack(["2", "3", "4"])
    print(s)
    s.push("5")
    print(s)
    s.pop()
    print(s, s.top)
