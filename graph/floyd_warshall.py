def floyd_warshall(adj_matrix):
    """Floyd-Warshall algorithm for all-pairs shortest paths.
    Time Complexity: O(V^3)
    Space Complexity: O(V^2)
    """
    
    n = len(adj_matrix)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize distances
    for i in range(n):
        for j in range(n):
            dist[i][j] = adj_matrix[i][j]
    
    # Floyd-Warshall core
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_matrix(matrix):
    for row in matrix:
        print([x if x != float('inf') else 'INF' for x in row])

if __name__ == "__main__":
    adj_matrix = [
        [0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(adj_matrix)
    print("All-pairs shortest distances:")
    print_matrix(result)
