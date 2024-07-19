# A DOUBLE ENDED QUEUE - ALLOWS TO ADD OR REMOVE ITEMS ON BOTH ENDS OF THE QUEUE, NOT FOLLOWING FIFO
from collections import deque

"""A deque is already implemented in python. It is more effective than a list because: - Lists are not thread safe (
two threads accessing one list could end up in errors - Adding elements to the beginning of the list is slower. It 
works by shifting each element one space further, making the time complexity of this action O(n) - for large lists it 
will take a long time. 

A Deque is essentially a DoubleLinkedList, this means that each element holds references to the next and previous 
elements, allowing for efficient insertion and removal of elements. The time complexity of such action is thus O(1)."""

# Initialize a deque giving it an iterable as its element
dqueue = deque(["d", "v", "o", "t"])

# Deque functions:
dqueue.append("z")
print(dqueue)
dqueue.appendleft("a")
print(dqueue)
dqueue.pop()
print(dqueue)
dqueue.popleft()
print(dqueue)

dqueue.extend(["x", "y"]) # Appends elements from an iterable to the right end of the deque.
print(dqueue)
dqueue.extendleft([0, 1, 2]) # Appends elements from an iterable to the left end of the deque. The elements are added in reverse order.
print(dqueue)
dqueue.reverse() # Reverses the elements of the deque in-place.
print(dqueue)
dqueue.rotate(2) # Rotates the deque n steps to the right. If n is negative, it rotates to the left.
print(dqueue)

# Create a deque with a maximum length of 3
deque_ = deque(maxlen=3)

# Add elements
deque_.append('A')
deque_.append('B')
deque_.append('C')
deque_.append('D')  # 'A' is automatically discarded

print(deque_)  # deque(['B', 'C', 'D'], maxlen=3)
