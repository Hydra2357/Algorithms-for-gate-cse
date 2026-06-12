from collections import defaultdict, deque

def topological_sort_kahn(adj_list, num_vertices):
    """Kahn's algorithm for topological sorting (BFS-based).
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    in_degree = [0] * num_vertices
    
    # Calculate in-degrees
    for u in adj_list:
        for v in adj_list[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)
        
        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) != num_vertices:
        return None, "Cycle detected"
    
    return topo_order, None

def topological_sort_dfs(adj_list, num_vertices):
    """DFS-based topological sorting.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    visited = [False] * num_vertices
    stack = []
    
    def dfs(vertex):
        visited[vertex] = True
        for neighbor in adj_list.get(vertex, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(vertex)
    
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

if __name__ == "__main__":
    adj_list = defaultdict(list)
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    
    for u, v in edges:
        adj_list[u].append(v)
    
    topo_kahn, error = topological_sort_kahn(adj_list, 6)
    print(f"Topological order (Kahn): {topo_kahn}")
    
    topo_dfs = topological_sort_dfs(adj_list, 6)
    print(f"Topological order (DFS): {topo_dfs}")
