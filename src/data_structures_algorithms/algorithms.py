from collections import deque

# MUTABLE
lists = [1, 2, 3, 4, 5]
sets = {1, 2, 3}
dicts = {1: 2, 2: 3, 3: 4}
# IMMUTABLE
strings = "Python"
ints = 2
frozensets = frozenset([1, 2, 3])
tuples = (1, 2, 3)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

unsorted_list = [5, 3, 2, 4, 1]

# Arrays and Linked Lists

# Heaps, Stacks, Queues
# https://ioflood.com/blog/using-deque-in-python-python-queues-and-stacks-made-easy/#:~:text=Deque%20is%20a%20Python%20function,safer%20choice%20for%20multithreaded%20programs.

# Hash Tables
## IMPORTANT

# Binary Search Trees

# N - ary Trees

# Trie - Trees

# IMPORTANT - KNOW WHAT IS INORDER, POSTORDER AND PREORDER

# Graphs
# DFS and BFS
# Dijkstra or A*

# Travelling Salesman Problem.....
# Knapsack Problem
# N choose K Problems
# Recursion


# Search Algorithms
# COMPLEXITIES:  where N is the size of the list

## Constant: Θ(1)
## Logarithmic: Θ(log N)
## Linear: Θ(N)
## Polynomial: Θ(N^2)
## Exponential: Θ(2^N)
## Factorial: Θ(N!)

## Linear Search - Complexity: O(N)
"""Linear search is a simple search algorithm that searches for an item by examining each element in a list one by 
one until it finds the item or determines that it is not in the list. """


def linear_search(lst, item):
    for i in lst:
        if i == item:
            return i, lst.index(i)
    return None


## Binary Search - Complexity: O(log N)
"""Binary search is an efficient search algorithm that searches for an item in a sorted list by dividing the list in 
half at each step and comparing the item to the middle element. If the item is less than the middle element, 
the search continues in the left half of the list; if it is greater, the search continues in the right half.
This process is repeated until the item is found or it is determined that it is not in the list. """


def binary_search_of_a_sorted_list(lst, item):
    lowest_index = 0
    highest_index = len(lst) - 1

    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        guess = lst[middle_index]
        if item > guess:
            lowest_index = middle_index + 1
        elif item < guess:
            highest_index = middle_index - 1
        else:
            return middle_index
    return None


# print(binary_search_of_a_sorted_list(lst, 4))


## Depth-first Search - Complexity: O(V+E) where V is number of vertices and E of edges
"""Depth-first search (DFS) is an algorithm that traverses a tree or graph by exploring as far as possible along each 
branch before backtracking. It is useful for searching a large, complex data structure or for finding a path between 
two nodes in a graph. """


def depth_first_search(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        a = graph[vertex] - set(path)
        for next in a:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# print(list(depth_first_search(graph, 'A', 'F')))  # Output: [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

## Breadth-first Search - Complexity: O(V+E) where V is number of vertices and E of edges
"""Breadth-first search (BFS) is an algorithm for searching a tree or graph data structure. 
It starts at the root node and explores all the nodes at the current level before moving on to the next level."""


def breadth_first_search(graph, start_node, end_node):
    visited = set()
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()  # Remove from the front of the queue
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == end_node:
                    return True
                else:
                    queue.append(adjacent)
        visited.add(node)
    return False


# print(breadth_first_search(graph, 'A', 'F'))  # Output: {'A', 'B', 'C', 'D', 'E', 'F'}


def bidirectional_search(graph, start_node, end_node):
    to_visit = deque([start_node, end_node])
    visited_from_start = {start_node}
    visited_from_end = {end_node}

    while to_visit:
        node = to_visit.popleft()
        if node in visited_from_start and node in visited_from_end:
            return True

        for adjacent in graph[node]:
            if node in visited_from_start and adjacent not in visited_from_start:
                visited_from_start.add(adjacent)
                to_visit.append(adjacent)
            if node in visited_from_end and adjacent not in visited_from_end:
                visited_from_end.add(adjacent)
                to_visit.append(adjacent)
    return False


# Sorting Algorithms
## Bubble Sort
"""Bubble sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in 
the wrong order. It continues this process until the list is sorted. """


def bubble_sort(lst):
    for first in range(len(lst) - 1):
        for second in range(len(lst) - 1 - first):
            if lst[second] > lst[second + 1]:
                lst[second], lst[second + 1] = lst[second + 1], lst[second]
    return lst


# print(bubble_sort(unsorted_list)) # Output: [1, 2, 3, 4, 5]

## Insertion Sort
"""Insertion sort is a simple sorting algorithm that builds the final sorted list one element at a time by comparing 
each element to the ones that come before it and inserting it into the correct position. """


def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
    return lst


# print(insertion_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]

## Selection Sort
"""Selection sort is a simple sorting algorithm that repeatedly selects the minimum element from the unsorted part of 
the list and appends it to the sorted part. """


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# print(selection_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]


## Merge Sort
"""Merge sort is a divide-and-conquer sorting algorithm that recursively splits the list in half, sorts the halves, 
and then merges them back together. """


def merge_sort():
    pass
