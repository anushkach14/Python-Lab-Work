import heapq

def dijkstra(adj_list, start):
    # Initialize distances to infinity for each node, except the start node
    distances = {node: float('inf') for node in adj_list}
    distances[start] = 0

    # Priority queue to track nodes and their current shortest distance
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a shorter distance to current_node is already found
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors and update distances if a shorter path is found
        for neighbor, weight in adj_list[current_node]:  # Iterate over neighbors and their weights
            distance = current_distance + weight

            # If a shorter path to neighbor is found, update distance and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f"To {node}: {distance}")
