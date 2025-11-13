from collections import deque


def count_graph_vertices_edges(graph) -> tuple[int, int]:
    vertices = len(graph.keys())
    sum_of_degrees = 0

    for key, value in graph.items():
        sum_of_degrees += len(value)

    edges = sum_of_degrees // 2

    return vertices, edges


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
# Hash Tables
# Binary Search Trees
# N - ary Trees
# Trie - Trees

# IMPORTANT - KNOW WHAT IS INORDER, POSTORDER AND PREORDER

# Graphs
# DFS and BFS
# Dijkstra or A*

# TODO: IMPLEMENT IN THE COMPLEX ALGORITHMS SECTION
# Travelling Salesman Problem.....
# Knapsack Problem
# N choose K Problems
# Recursion


# Search Algorithms
# COMPLEXITIES:  where N is the size of the list

# Constant: Θ(1)
# Logarithmic: Θ(log N)
# Linear: Θ(N)
# Polynomial: Θ(N^2)
# Exponential: Θ(2^N)
# Factorial: Θ(N!)


def linear_search(lst: list, item: int) -> list or None:
    """
    Linear search is a simple search algorithm that searches
    for an item by examining each element in a list one by one
    until it finds the item or determines that it is not in the list.
    Complexity: O(N)
    """
    for i in lst:
        if i == item:
            return i, lst.index(i)
    return None


# print(linear_search(lst, 4))


def binary_search_of_a_sorted_list(lst: list, item: int) -> list or None:
    """
    Binary search is an efficient search algorithm that searches for an item
    in a sorted list by dividing the list in half at each step
    and comparing the item to the middle element. If the item is less than the middle element,
    the search continues in the left half of the list; if it is greater,
    the search continues in the right half.
    Complexity: O(log N)
    """
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


def depth_first_search(graph: dict, start: int, goal: int) -> list:
    """
    Depth-first search (DFS) is an algorithm that traverses a tree or graph
    by exploring as far as possible along each branch before backtracking.
    It is useful for searching a large, complex data structure
    or for finding a path between two nodes in a graph.
    Complexity: O(V+E) where V is number of vertices and E of edges
    """
    visited = set()
    stack = [start]
    path = []
    while stack:
        node = stack.pop()
        if node not in visited:
            path.append(node)
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    stack.append(adjacent)
    return path


# print(list(depth_first_search(graph, 'A', 'F')))  # Output: ['A', 'B', 'E', 'F', 'C', 'D']


def breadth_first_search(graph: dict, start: int, goal: int) -> list:
    """
    Breadth-first search (BFS) is an algorithm for searching a tree or graph data structure.
    It starts at the root node and explores all the nodes at the current level
    before moving on to the next level.
    Complexity: O(V+E) where V is number of vertices and E of edges
    """
    visited = set()
    queue = deque([start])
    path = []
    while queue:
        node = queue.popleft()  # Remove from the front of the queue
        if node not in visited:
            path.append(node)
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    queue.append(adjacent)
    return path


# print(breadth_first_search(graph, 'A', 'F'))  # Output: ['A', 'C', 'B', 'F', 'E', 'D']


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


def bubble_sort(lst):
    """
    Bubble sort is a simple sorting algorithm that repeatedly
    compares adjacent elements and swaps them if they are in the wrong order.
    It continues this process until the list is sorted.
    Complexity: O(n^2)
    """
    for first in range(len(lst) - 1):
        for second in range(len(lst) - 1 - first):
            if lst[second] > lst[second + 1]:
                lst[second], lst[second + 1] = lst[second + 1], lst[second]
    return lst


# print(bubble_sort(unsorted_list)) # Output: [1, 2, 3, 4, 5]


def insertion_sort(lst):
    """
    Insertion sort is a simple sorting algorithm that builds
    the final sorted list one element at a time by comparing
    each element to the ones that come before it
    and inserting it into the correct position.
    Complexity: O(n^2)
    """
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
    return lst


# print(insertion_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]


def selection_sort(lst):
    """
    Selection sort is a simple sorting algorithm that repeatedly
    selects the minimum element from the unsorted part of
    the list and appends it to the sorted part.
    Complexity: O(n^2)
    """
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# print(selection_sort(unsorted_list))  # Output: [1, 2, 3, 4, 5]


def merge_sort():
    """
    Merge sort is a divide-and-conquer sorting algorithm
    that recursively splits the list in half, sorts the halves,
    and then merges them back together.
    Complexity: O(n log(n))
    """
    pass
