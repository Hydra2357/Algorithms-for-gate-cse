from collections import defaultdict

def hungarian_algorithm(cost_matrix):
    """Hungarian algorithm for assignment problem.
    Finds minimum cost perfect matching in bipartite graph.
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    
    n = len(cost_matrix)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)
    
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [float('inf')] * (n + 1)
        used = [False] * (n + 1)
        
        while p[j0] != 0:
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            used[j0] = True
            
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost_matrix[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            
            j0 = j1
        
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    
    assignment = [0] * n
    for j in range(1, n + 1):
        if p[j] != 0:
            assignment[p[j] - 1] = j - 1
    
    return assignment

if __name__ == "__main__":
    cost_matrix = [
        [4, 1, 3],
        [2, 0, 5],
        [3, 2, 2]
    ]
    
    assignment = hungarian_algorithm(cost_matrix)
    print(f"Assignment: {assignment}")
