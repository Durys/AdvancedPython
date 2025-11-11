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
