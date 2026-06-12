def kruskal_algorithm(edges, num_vertices):
    """Kruskal's algorithm for Minimum Spanning Tree.
    Greedy approach using Union-Find.
    Time Complexity: O(E log E)
    Space Complexity: O(V + E)
    """
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]
        
        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            
            if root_x == root_y:
                return False
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            return True
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []
    total_cost = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
    
    return mst, total_cost

if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2)
    ]
    mst, cost = kruskal_algorithm(edges, 5)
    print(f"MST edges: {mst}")
    print(f"Total cost: {cost}")
