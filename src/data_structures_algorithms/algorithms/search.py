"""Search Algorithms"""
from collections import deque
from typing import Any


def count_graph_vertices_edges(graph) -> tuple[int, int]:
    vertices = len(graph.keys())
    sum_of_degrees = 0

    for key, value in graph.items():
        sum_of_degrees += len(value)

    edges = sum_of_degrees // 2

    return vertices, edges


def linear_search(lst: list, item: int) -> tuple[Any, int] | None:
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



def binary_search_of_a_sorted_list(lst: list, item: int) -> list | None:
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


def depth_first_search(graph: dict, start: int|str, goal=None) -> list:
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


def breadth_first_search(graph: dict, start: int|str, goal=None) -> list:
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


def bidirectional_search(graph: dict, start_node: int|str, end_node: int|str) -> bool:
    """
    Bidirectional search runs two simultaneous searches:
    one forward from the start and one backward from the goal.
    Complexity: O(b^(d/2))
    - b (branching factor): Average number of children per node.
    - d (distance): Minimum number of edges between start and goal.
    """
    if start_node == end_node:
        return True

    # Frontiers for BFS from start and end
    start_frontier = {start_node}
    end_frontier = {end_node}

    # Visited sets to avoid cycles and redundant work
    start_visited = {start_node}
    end_visited = {end_node}

    while start_frontier and end_frontier:
        # Check for intersection
        if start_frontier and end_frontier:
            return True

        # Expand from start
        next_start_frontier = set()
        for node in start_frontier:
            for neighbor in graph.get(node, []):
                if neighbor not in start_visited:
                    start_visited.add(neighbor)
                    next_start_frontier.add(neighbor)
        start_frontier = next_start_frontier

        # Check for intersection again
        if start_frontier and end_frontier:
            return True

        # Expand from end
        next_end_frontier = set()
        for node in end_frontier:
            for neighbor in graph.get(node, []):
                if neighbor not in end_visited:
                    end_visited.add(neighbor)
                    next_end_frontier.add(neighbor)
        end_frontier = next_end_frontier

    return False


if __name__ == "__main__":
    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F'},
             'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}
             }

    unsorted_list = [5, 3, 2, 4, 1]
    sorted_list = [2, 3, 4, 5, 6]

    print(linear_search(unsorted_list, 4))
    print(binary_search_of_a_sorted_list(sorted_list, 4))
    print(list(depth_first_search(graph, 'A', 'F')))  # Output: ['A', 'B', 'E', 'F', 'C', 'D']
    print(breadth_first_search(graph, 'A', 'F'))  # Output: ['A', 'C', 'B', 'F', 'E', 'D']
    print(bidirectional_search(graph, 'A', 'F'))
