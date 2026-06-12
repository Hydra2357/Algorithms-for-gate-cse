import heapq
from collections import defaultdict

def prim_algorithm(adj_list, start_vertex):
    """Prim's algorithm for Minimum Spanning Tree.
    Greedy approach using min-heap.
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V + E)
    """
    
    visited = set()
    mst = []
    total_cost = 0
    min_heap = [(0, start_vertex, -1)]  # (weight, vertex, parent)
    
    while min_heap and len(visited) < len(adj_list):
        weight, vertex, parent = heapq.heappop(min_heap)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        if parent != -1:
            mst.append((parent, vertex, weight))
            total_cost += weight
        
        for neighbor, edge_weight in adj_list[vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, vertex))
    
    return mst, total_cost

if __name__ == "__main__":
    # Adjacency list representation
    adj_list = defaultdict(list)
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2)
    ]
    
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    mst, cost = prim_algorithm(adj_list, 0)
    print(f"MST edges: {mst}")
    print(f"Total cost: {cost}")
