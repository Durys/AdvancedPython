from collections import deque

"""
A data scientist is working on a new algorithm to analyze
user behavior.The algorithm takes multiple sequences of numbers as input, e.g.:
1, 2, 15, 8
2, 4, 7, 8
The goal is to create a single consolidated sequence of numbers
that preserves the ** ordering of each input sequence **.
The data scientist wants to know if such a consolidated sequence is possible.
For the above example, 1, 2, 4, 7, 15, 8 is a valid consolidation.

Another valid solution: 1, 2, 4, 15, 7, 8
"""

consolidation = []

d = {
    1: [2],
    2: [15, 4],
    15: [8],
    7: [8],
    4: [7],
    8: []
}


def check_for_loop(d):
    def dfs(k):
        visited = set()
        visited.add(k)
        stack = [k]
        while stack:
            i = stack.pop()
            for adj in d[i]:
                if adj not in visited:
                    visited.add(adj)
                    stack.append(adj)
                else:
                    return True, visited
        return False, visited

    for k in d.keys():
        is_possible, sol = dfs(k)

        if is_possible and len(sol) == len(d.keys()):
            return sol

    return {}


print(check_for_loop(d))


# Define states for cycle detection
UNVISITED = 0
VISITING = 1
VISITED = 2


def topological_sort_dfs(graph):
    all_nodes = list(graph.keys())
    for neighbors in graph.values():
        for node in neighbors:
            if node not in all_nodes:
                all_nodes.append(node)

    visited_states = {node: UNVISITED for node in all_nodes}
    result = deque()

    def dfs(node):
        visited_states[node] = VISITING

        for neighbor in sorted(graph.get(node, [])):
            if visited_states[neighbor] == UNVISITED:
                if not dfs(neighbor):
                    return False
            elif visited_states[neighbor] == VISITING:
                return False

        visited_states[node] = VISITED
        result.appendleft(node)

        return True

    for node in all_nodes:
        if visited_states[node] == UNVISITED:
            if not dfs(node):
                return None

    return list(result)


print("--- Graph with a valid solution ---")
solution1 = topological_sort_dfs(d)
if solution1:
    print(f"Valid sequence: {solution1}\n")
else:
    print("No valid sequence possible (cycle detected).\n")

d_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print("--- Graph with a cycle ---")
solution2 = topological_sort_dfs(d_cycle)
if solution2:
    print(f"Valid sequence: {solution2}")
else:
    print("No valid sequence possible (cycle detected)")
