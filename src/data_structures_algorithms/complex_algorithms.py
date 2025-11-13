import heapq


def dijkstra(graph: dict, start_node: int) -> dict:
    """
    Finds the shortest path from a start node
    to all other nodes in a weighted graph.
    """
    if start_node not in graph:
        return {}
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def count_islands(grid: list[list[int]]) -> int:
    """
    A recursion example using dfs - shows how many
    isolated "islands" there are in an array.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return

        grid[r][c] = 0

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c)
                islands += 1

    return islands


if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 5, 'C': 3},
        'E': {}
    }

    shortest_paths = dijkstra(graph, 'A')

    print("Shortest paths from node 'A':")
    for node, distance in shortest_paths.items():
        print(f"  Distance to {node}: {distance}")

    map = [
        [1, 1, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 0]
    ]

    copied_map = [row[:] for row in map]

    print(f"There are {count_islands(copied_map)} islands in the map {map}")

