from collections import defaultdict, deque

def bellman_ford(adj_list, start, num_vertices):
    """Bellman-Ford algorithm for shortest paths.
    Handles negative edge weights and detects negative cycles.
    Time Complexity: O(VE)
    Space Complexity: O(V)
    """
    
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(num_vertices - 1):
        for u in adj_list:
            for v, weight in adj_list[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u in adj_list:
        for v, weight in adj_list[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None, "Negative cycle detected"
    
    return distances, None

if __name__ == "__main__":
    adj_list = defaultdict(list)
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, -3),
        (2, 3, 2),
        (1, 3, 5)
    ]
    
    for u, v, w in edges:
        adj_list[u].append((v, w))
    
    distances, error = bellman_ford(adj_list, 0, 4)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Shortest distances from 0: {distances}")
